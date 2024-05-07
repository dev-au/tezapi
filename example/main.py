from aioapi import AioAPI, Request
from aioapi.exceptions import APIError, ClassBaseError
from aioapi.schemas import SchemaModel
from aioapi.templating import Jinja2Template

app = AioAPI()

render = Jinja2Template('templates')


# path var and template response and raise error
# ///////////////////////////////////////
@app.get("/hello/{name}")
async def hello(name: str):
    if name == "John":
        raise APIError('NameError', 400, 'You were blocked')
    return render('home.html', {'name': name})


# ///////////////////////////////////////

# raise class based errors

class UsernameError(ClassBaseError):
    status_code = 400
    message = 'You were blocked from well hello'


@app.get('/good-hello/{name}')
async def good_hello(name: str):
    if name == "John":
        raise UsernameError()
    return render('home.html', {'name': name})


# ///////////////////////////////////////

# use models

class UserModel(SchemaModel):
    username: str
    phone_number: int = None
    password: str


@app.post('/user-signup')
async def user_info(request: Request):
    data = UserModel(request)
    await data.form_validate()
    return data

app.run()
