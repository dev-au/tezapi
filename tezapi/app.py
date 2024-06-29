from aiohttp import web
from aiohttp.web_request import Request

from .middleware import Middleware
from .router_field import Router
from .routes import Route


class TezAPI:
    def __init__(self, host: str = '127.0.0.1', port: int = 8000):
        self.app = web.Application()
        self.host = host
        self.port = port
        self.routes = []
        self.middlewares: list[Middleware] = []

    def _add_route(self, path, handler, method: str, **kwargs):
        self.routes.append(web.route(method, path, handler, **kwargs))

    def get(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                mid_result = await self._run_middleware(request)
                if mid_result is not None:
                    return mid_result
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def post(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                mid_result = await self._run_middleware(request)
                if mid_result is not None:
                    return mid_result
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'POST', name=func.__name__)
            return decorated

        return wrapper

    def delete(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                mid_result = await self._run_middleware(request)
                if mid_result is not None:
                    return mid_result
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'DELETE', name=func.__name__)
            return decorated

        return wrapper

    def put(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                mid_result = await self._run_middleware(request)
                if mid_result is not None:
                    return mid_result
                route = Route(func)
                return await route(request)

            self._add_route(path, decorated, 'PUT', name=func.__name__)
            return decorated

        return wrapper

    def middleware(self, path: str = '*', method: str = '*'):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self.middlewares.append(Middleware(decorated, path, method))
            return decorated

        return wrapper

    def _run_router_functions(self, router):
        async def decorated(request: Request):
            mid_result = await self._run_middleware(request)
            if mid_result is not None:
                return mid_result
            route = router['handler']
            return await route(request)

        self._add_route(router['path'], decorated, router['method'], name=router['name'])

        return decorated

    async def _run_middleware(self, request: Request):
        for middleware in self.middlewares:
            print(request.path.startswith(middleware.path[:-1]))

            if (middleware.path == request.path or middleware.path == '*') and (
                    middleware.method == request.method or middleware.method == '*') or (
                    middleware.path[-1] == '*' and request.path.startswith(middleware.path[:-1])):
                result = await middleware.route(request)
                if result is not None:
                    return result

    def __add__(self, router: Router):
        self.middlewares += router.middlewares
        for route in router.routes:
            self._run_router_functions(route)

        return self

    def run(self):
        self.app.add_routes(self.routes)
        web.run_app(self.app, host=self.host, port=self.port)
