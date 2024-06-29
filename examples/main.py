from router1 import router
from tezapi import TezAPI, Request
from tezapi.schemas import SchemaModel
from tezapi.templating import Jinja2Template

app = TezAPI()
render = Jinja2Template('templates')


@app.middleware()
async def middleware_handler(request: Request):
    print('Middleware started')
    return 'Breaking router'


class UserSchema(SchemaModel):
    username: str
    phone_number: str


@app.get('/test')
async def test(request: Request):
    return 'Working main test'


app += router

app.run()
