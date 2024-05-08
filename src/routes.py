import inspect
import logging

from aiohttp.web_request import Request

from src.exceptions import APIError, InternalServerError, ClassBaseError
from src.responses import JSONResponse, HTMLResponse

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d')


class Route:

    def __init__(self, handler):
        self.handler = handler
        signature = inspect.signature(handler)
        arguments = {}
        for parameter in signature.parameters.values():
            arguments[parameter.name] = parameter.annotation
        self.arguments = arguments
        self.signature = signature

    async def __call__(self, request: Request):
        try:
            request_path_data = self._request_path(request)
        except APIError as error:
            return error.__response__
        try:
            result = await self.handler(**request_path_data)
            if isinstance(result, dict):
                return JSONResponse(result).__response__
            try:
                return result.__response__
            except AttributeError:
                return HTMLResponse(result).__response__
        except APIError as error:
            return error.__response__
        except ClassBaseError as error:
            return error.__response__


    def _request_path(self, request: Request):
        data = {}
        for key, value in self.arguments.items():
            item = request.match_info.get(key)
            if value == Request:
                item = request
            elif value == int:
                try:
                    item = int(item)
                except ValueError:
                    raise APIError('PathValidationError', 400, f'{key} is must be an integer')
            elif value == float:
                try:
                    item = float(item)
                except ValueError:
                    raise APIError('PathValidationError', 400, f'{key} must be a float')
            data[key] = item
        return data
