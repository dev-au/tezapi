import inspect

from aiohttp.web_request import Request

from httpexception import InternalServerError, APIException


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
        request_path_data = self._request_path(request)
        api_exception_occurred = False
        try:
            return await self.handler(**request_path_data)
        except APIException as error:
            print(error)
        finally:
            print('nooooo')

    def _request_path(self, request: Request):
        data = {}
        for key, value in self.arguments.items():
            item = request.match_info.get(key)
            if value == Request:
                item = request
            elif value == int:
                item = int(item)
            elif value == float:
                item = float(item)
            data[key] = item
        return data
