from example_schemas import UserSchema, CarSchema
from tezapi import TezAPI, Request
from tezapi.templating import Jinja2Template

app = TezAPI()
render = Jinja2Template('templates')


@app.middleware
async def middleware_handler(request: Request, call_next):
    print('Middleware started')
    response = await call_next(request)
    print('Middleware finished')
    return response


@app.post("/")
async def hello(user: UserSchema, car: CarSchema):
    print(user)
    return car


app.run()
