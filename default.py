from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def handle(request: Request):
    data = await request.json()
    print(data.items())
    name = data.get('name')
    # text = 1 + name
    return web.Response(text=name + 'efdf')


app = web.Application()
app.add_routes([web.post('/', handle),
                web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app)
