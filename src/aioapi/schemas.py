from json import JSONDecodeError as JSONDecodeException

from aiohttp.web_request import Request

from .exceptions import JSONDecodeError, APIError
from .responses import JSONResponse


class SchemaModel:
    def __init_subclass__(cls, **kwargs):
        cls.__fields__ = cls.__annotations__

    def __init__(self, request: Request):
        self._request = request

    @property
    def __response__(self):
        result = self.__dict__
        del result['_request']
        return JSONResponse(result).__response__

    def _parse_model(self, data):
        for key, annotate in self.__fields__.items():
            if key in data:
                try:
                    item = annotate(data.get(key))
                    self.__setattr__(key, item)
                except ValueError:
                    raise APIError('FieldTypeError', 400, f'{key.title()} is must be a {annotate.__name__}')
            else:
                if not hasattr(self, key):
                    raise APIError('FieldTypeError', 400, f'{key.title()} must be provided')
        return self

    async def json_validate(self):
        try:
            data = await self._request.json()
            self._parse_model(data)
        except JSONDecodeException:
            raise JSONDecodeError()

    async def form_validate(self):
        try:
            data = await self._request.post()
            self._parse_model(data)
        except JSONDecodeException:
            raise JSONDecodeError()
