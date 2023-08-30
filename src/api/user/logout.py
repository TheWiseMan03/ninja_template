
from src.apps.user.schemas.logout import LogoutSchema
from lib.jwt import blacklist_refresh_token
from django.http import HttpRequest

response = { 204: None }


async def handler(request: HttpRequest, payload: LogoutSchema):
    await blacklist_refresh_token(payload.refresh)
   
    return 204, None