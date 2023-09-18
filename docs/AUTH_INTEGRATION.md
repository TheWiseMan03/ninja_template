

## The provided code snippet is responsible for the process of authenticating users and issuing access and refresh tokens to them after successful authentication.




```bash
from ninja.schema import Schema
```

### Create data structures for information serialization processes: `schema.py`
```bash
class LoginSchema(Schema):
    username: str
    password: str

class LoginResponseSchema(Schema):
    refresh: str
    access: str

class LogoutSchema(Schema):
    refresh: str
```



### Defining an Authentication Handler Using an Asynchronous Approach: `login.py`
```bash
from django.contrib.auth import authenticate
from ninja.errors import ValidationError
from .schemas import LoginResponseSchema, LoginSchema
from lib.jwt import get_tokens_for_user
from asgiref.sync import sync_to_async


# Define the response scheme for successful authentication
response = LoginResponseSchema

# Asynchronous handler to perform user authentication
async def handler(request, payload: LoginSchema):
# Authenticate the user using the entered username and password
    user = await sync_to_async(authenticate)(request, username=payload.username, password=payload.password)

    # If the user has not been authenticated (user is None), raise a ValidationError exception
    if user is None:
        raise ValidationError("Invalid username or password")
    
    # Create and return access and refresh tokens for a successfully authenticated user
    return await sync_to_async(get_tokens_for_user)(user)
```

### Define an asynchronous handler for the logout process: `logout.py`
```bash

from lib.jwt import blacklist_refresh_token
from .schemas import LogoutSchema

response = { 204: None }

# This handler logs the user out and adds the refresh token to the blacklist.
async def handler(request, payload: LogoutSchema):
    # Add the refresh token to the blacklist (logout procedure)
    await blacklist_refresh_token(payload.refresh)
    # Return a tuple containing the HTTP response code (204 - No Content) and an empty value
    return 204, None
```