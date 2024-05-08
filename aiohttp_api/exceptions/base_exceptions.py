from aiohttp_api.exceptions.apiexception import ClassBaseError


class InternalServerError(ClassBaseError):
    status_code = 500


class JSONDecodeError(ClassBaseError):
    status_code = 400
    message = 'JSON decode error'
