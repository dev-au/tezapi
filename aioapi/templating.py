import jinja2

from aioapi.responses import HTMLResponse


class Jinja2Template:

    def __init__(self, path: str):
        self.templates_env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))

    def __call__(self, page: str, context: dict):
        template = self.templates_env.get_template(page)
        rendered_template = template.render(context)
        return HTMLResponse(rendered_template)
