from aioapi import AioAPI, Request
from aioapi.httpexception import SampleException

app = AioAPI()


@app.get('/hello/{name}')
async def hello(request: Request, name: str):
    raise SampleException()


app.run()
