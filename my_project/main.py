from aioapi import AioAPI, Request
from my_exceptions import SampleException1
from aioapi.httpexception import SampleException2

app = AioAPI()


@app.get('/hello/{name}')
async def hello(request: Request, name: str):
    raise SampleException2()


app.run()
