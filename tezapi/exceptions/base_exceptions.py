from .apiexception import ClassBaseError


class InternalServerError(ClassBaseError):
    status_code = 500
    message = 'Internal Server Error'


class JSONDecodeError(ClassBaseError):
    status_code = 400
    message = 'JSON decode error'


class PageNotFoundError(ClassBaseError):
    status_code = 404
    message = 'Page not found error'
