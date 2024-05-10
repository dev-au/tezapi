import json

from aiohttp.web_fileresponse import FileResponse as _FileResponse
from aiohttp.web_response import Response as _Response


class Response:
    def __init__(self, content: str, status_code: int, content_type: str, headers: dict = None):
        self.content = content
        self.status_code = status_code
        self.content_type = content_type
        self.headers = headers

    @property
    def __response__(self):
        return _Response(text=self.content, status=self.status_code, content_type=self.content_type,
                         headers=self.headers)


class HTMLResponse(Response):
    def __init__(self, html_content: str, status_code: int = 200, headers: dict = None):
        super().__init__(content=html_content, status_code=status_code, content_type='text/html',
                         headers=headers)


class JSONResponse(Response):
    def __init__(self, json_content: dict, status_code: int = 200, headers: dict = None):
        json_data = {
            'error': {
                'name': None,
                'message': None
            },
            'data': json_content
        }
        super().__init__(content=json.dumps(json_data), status_code=status_code, content_type='application/json',
                         headers=headers)


class FileResponse:
    def __init__(self, file_path: str, status_code: int = 200, headers: dict = None):
        self.__response__ = _FileResponse(file_path, status=status_code, headers=headers)
