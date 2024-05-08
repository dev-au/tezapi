from aiohttp import web
from aiohttp.web_request import Request

from .routes import Route


class TezAPI(web.Application):
    def __init__(self, host: str = '127.0.0.1', port: int = 8000, **kwargs):
        self.host = host
        self.port = port
        self.routes = []
        super().__init__(**kwargs)

    def _add_route(self, path, handler, method: str, **kwargs):
        self.routes.append(web.route(method, path, handler, **kwargs))

    def get(self, path: str, **kwargs):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'GET', name=func.__name__, **kwargs)
            return decorated

        return wrapper

    def post(self, path: str, **kwargs):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'POST', name=func.__name__, **kwargs)
            return decorated

        return wrapper

    def delete(self, path: str, **kwargs):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'DELETE', name=func.__name__, **kwargs)
            return decorated

        return wrapper

    def put(self, path: str, **kwargs):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'PUT', name=func.__name__, **kwargs)
            return decorated

        return wrapper

    def run(self):
        app = self
        app.add_routes(self.routes)
        web.run_app(app, host=self.host, port=self.port)
