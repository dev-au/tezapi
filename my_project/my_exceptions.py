from httpexception import APIException


class SampleException1(APIException):
    def __init__(self):
        super().__init__(name='SampleException', status_code=400)