

from django.contrib.auth import authenticate
from ninja.errors import ValidationError
from src.apps.user.schemas.login import LoginResponseSchema, LoginSchema

from lib.jwt import get_tokens_for_user
from asgiref.sync import sync_to_async


response = LoginResponseSchema
auth = None


async def handler(request, payload: LoginSchema):
    user = await sync_to_async(authenticate)(request, username=payload.username, password=payload.password)

    if user is None:
        raise ValidationError("Invalid username or password")
    
    return await sync_to_async(get_tokens_for_user)(user)
