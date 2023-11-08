import ninja_jwt

from lib.logger import logger


def catch_errors(api_instance):
    @api_instance.exception_handler(Exception)
    def global_error_handler(request, exc):
        
        status = 500

        if isinstance(exc, ninja_jwt.exceptions.TokenError):
            status = 401

        if status == 500:
            logger.error(exc, exc_info=True)

        return api_instance.create_response(request, str(exc), status=status)
