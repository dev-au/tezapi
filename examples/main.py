from tezapi import TezAPI
from tezapi.templating import Jinja2Template

app = TezAPI()
render = Jinja2Template('templates')


# Define routes and handlers
@app.get("/{name}")
async def hello(name: str):
    return render("home.html", {"name": name})


# Run the aiohttp-api application
app.run()
