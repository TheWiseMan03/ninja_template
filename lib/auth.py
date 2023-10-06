from ninja_jwt.authentication import AsyncJWTAuth
from .logger import logger
from ninja.errors import HttpError


class CustomAsyncJWTAuth(AsyncJWTAuth):
    def __init__(self, permissions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permissions = permissions

    async def authenticate(self, request, token):
        user = await super().authenticate(request, token)
        if self.permissions:
            self.check_permissions(request, user)
        return user

    def get_permissions(self):
        return [permission() for permission in self.permissions]

    def check_permissions(self, request, user):
        for permission in self.get_permissions():
            if not permission.has_permission(request, user):
                raise HttpError(403, "Not allowed to do this operation")
        return True
