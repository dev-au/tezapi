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


from tezapi.schemas import SchemaModel


class UserSchema(SchemaModel):
    username: str
    phone_number: str


@app.post("/")
async def hello(user: UserSchema):
    print(user)
    return user


app.run()
