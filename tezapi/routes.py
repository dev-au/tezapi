import inspect
import logging
from json import JSONDecodeError as JSONDecodeException

from aiohttp.web_request import Request

from .exceptions import APIError, ClassBaseError, JSONDecodeError
from .responses import JSONResponse, HTMLResponse
from .schemas import SchemaModel

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
            request_path_data = await self._request_annotations(request)
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

    async def _request_annotations(self, request: Request):
        try:
            json_data = await request.json()
        except JSONDecodeException:
            raise JSONDecodeError()
        data = {}
        for key, value in self.arguments.items():
            if issubclass(value, SchemaModel):
                item = value(json_data)
            elif value == Request:
                item = request
            else:
                item = request.match_info.get(key)
                if value == int:
                    try:
                        item = int(item)
                    except ValueError:
                        raise APIError('PathValidationError', 400, f'{value.__name__} {key} is must be an integer')
                elif value == float:
                    try:
                        item = float(item)
                    except ValueError:
                        raise APIError('PathValidationError', 400, f'{value.__name__} {key} must be a float')
            data[key] = item
        return data

