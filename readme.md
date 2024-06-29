# TezAPI

TezAPI is an asynchronous web framework for building powerful and efficient web APIs and applications with Python. It
leverages the asyncio and aiohttp libraries to provide a seamless development experience for building high-performance
web applications.

## Key Features

- Asynchronous by design: Built on top of asyncio and aiohttp, TezAPI allows you to write highly concurrent and
  efficient web applications.
- Simple and intuitive API: With minimal boilerplate and sensible defaults, TezAPI provides a clean and intuitive API
  for defining routes and handling requests.
- Error handling made easy: TezAPI simplifies error handling with support for both simple and class-based error
  responses, making it straightforward to handle exceptions and provide meaningful feedback to clients.
- Schema validation with SchemaModel: TezAPI makes form validation easy with the SchemaModel class, allowing you to
  validate incoming request data against defined schemas effortlessly.
- Template rendering with Jinja2Template: TezAPI includes built-in support for Jinja2Template, allowing you to render
  HTML templates seamlessly.

## Installation

You can install TezAPI via pip:

```commandline
pip install tezapi
```

## Quick Start

```python
import datetime
from tezapi import TezAPI
from tezapi.templating import Jinja2Template

app = TezAPI()
render = Jinja2Template('templates')


# Define routes and handlers
@app.get("/")
async def hello():
    return render('home.html', {'today': str(datetime.datetime.now())})


# Run the TezAPI application
app.run()
```

## Advanced Features and Best Practices

In addition to the basic setup and usage, TezAPI offers advanced features and best practices for building robust web
applications.

### Advanced Routing Techniques

#### Route Parameters

In TezAPI, you can define routes with parameters that capture dynamic values from the URL. For example:

```python
@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int):
    # Retrieve user data based on user_id
    return {'user_id': user_id}
```

### Additional routes

```python
from tezapi import Router

user_router = Router(prefix='/user')


@user_router.get('/get-me')
async def get_info(request):
    return {'name': 'John', 'surname': 'Doe'}
```

##### Include routers

```python
from users import user_router

# including is very easy
app += user_router
```

### Query Parameters

You can also handle query parameters in TezAPI routes. For example:

```python
@app.get("/search")
async def search_users(request: Request):
    query = request.query.get('q')
    # Perform search based on query parameter
    return {'query': query}
```

### Middleware

Middleware in TezAPI allows you to intercept and modify requests and responses before they reach the handler. You can
use middleware for tasks such as authentication, logging, and request/response manipulation.
Now optimized, you can install middleware filter selected request path and method

```python
@app.middleware(path='/user', method='GET')
async def middleware_1(request: Request):
    print('Middleware started')
    return response
```

And removed `call_next` if you use `return` and `call_next` automatically work

```python
@app.middleware()
async def middleware_2(request: Request):
    print('Middleware started')
    return response
```

If you empty middleware arguments, this means it work any methods and any paths

#### Router middleware

```python
@my_router.middleware()
async def auth_filter(request):
    return check(auth)
```

### Model Parameters

JSON Request models automatic filtering and validate

```python
from tezapi.schemas import SchemaModel


class UserSchema(SchemaModel):
    username: str
    phone_number: str


@app.post("/")
async def hello(user: UserSchema):
    print(user)
    return user
```

## Optimized SchemaModels -> coming soon
