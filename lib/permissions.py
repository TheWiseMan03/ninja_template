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

    def check_permissions(self, request, user):
        for permission in self.permissions:
            if not permission.check(request, user):
                raise HttpError(403, 'Not allowed to do this operation')
        return True


class BasePermission:

    def __and__(self, other):
        return AND(self, other)

    def __or__(self, other):
        return OR(self, other)



    @staticmethod
    def check(request, user):
        return False


class AND:
    def __init__(self, perm_1, perm_2):
        self.perm_1 = perm_1
        self.perm_2 = perm_2

    def check(self, request, user):
        return self.perm_1.check(request, user) and self.perm_2.check(request, user)


class OR:
    def __init__(self, perm_1, perm_2):
        self.perm_1 = perm_1
        self.perm_2 = perm_2

    def check(self, request, user):
        return self.perm_1.check(request, user) or self.perm_2.check(request, user)


class IsAdmin(BasePermission):

    @staticmethod
    def check(request, user):
        if user:
            return user.is_staff
        else:
            return False


class ReadOnly(BasePermission):

    @staticmethod
    def check(request, user):
        return request.method == 'GET'


class IsNameStartsWithA(BasePermission):

    @staticmethod
    def check(request, user):
        return user.username.startswith('a')


class IsAuthenticated(BasePermission):

    @staticmethod
    def check(request, user):
        return user.is_authenticated
