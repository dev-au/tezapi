import asyncio

from aiohttp.web_request import Request



class SchemaModel:
    def __init_subclass__(cls, **kwargs):
        cls.fields = cls.__annotations__

    @staticmethod
    async def json(request: Request):
        data = await request.json()

        print(data)
