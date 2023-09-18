# This function is a wrapper for creating a global error handler for the Ninja API. It accepts an [`api_instance`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/URLS_USAGE_GUIDE.md) to which the handler is applied.


```bash
import ninja_jwt  
from lib.logger import logger  

def catch_errors(api_instance):

    # Global error handler for the Ninja API.
    # api_instance (ninja.NinjaAPI): The Ninja API instance to which the handler is applied.

    @api_instance.exception_handler(Exception)
    def global_error_handler(request, exc):
        # Exception handler for global errors.

        status = 500 

        if isinstance(exc, ninja_jwt.exceptions.TokenError):
            # If an error occurs related to the JWT token, set the status to 401 (Unauthorized)
            status = 401

        if status == 500:
            # If the status remains 500, log the exception with additional information
            logger.error(exc, exc_info=True)

        # Create and return an API response with error text and set status1
        return api_instance.create_response(request, str(exc), status=status)

```

>`global_error_handler`: This is a nested function that is an exception handler for global errors in the Ninja API. It takes a request request and an exc exception, then determines the status of the response and creates an API response with error information and the set status.
>
>Depending on the type of exception, the handler sets the appropriate response status (for example, 401 for errors related to the JWT token). If the status remains 500 (Internal Server Error), then the handler also writes the exception to the log with additional information.
>
>Finally, the catch_errors function returns the created global_error_handler, which will be used to handle errors when making requests to the Ninja API.