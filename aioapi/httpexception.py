class APIException(Exception):
    def __init__(self, name: str, status_code: int, message: dict = None, headers: dict = None):
        exception_data = {
            'data': {
                'name': name,
                'status_code': status_code,
                'message': message
            },
            'status': status_code,
            'headers': headers
        }
        self.response = exception_data
        super().__init__(exception_data)


class InternalServerError(APIException):
    def __init__(self):
        super().__init__(name='InternalServerError', status_code=500)


class SampleException2(APIException):
    def __init__(self):
        super().__init__(name='SampleException', status_code=400)