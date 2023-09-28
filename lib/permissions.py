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
        for permission in self.get_permissions():
            if not permission.check(request, user):
                raise HttpError(403, 'Not allowed to do this operation')
        return True

    def get_permissions(self):
        return [permission() for permission in self.permissions]


class OperationHolderMixin:

    def __and__(self, other):
        return OperandHAndler(AND, self, other)

    def __or__(self, other):
        return OperandHAndler(OR, self, other)

    def __invert__(self):
        return SingleOperandHolder(NOT, self)


class SingleOperandHolder(OperationHolderMixin):
    def __init__(self, operation_type, perm1):
        self.operator_type = operation_type
        self.perm_class = perm1

    def __call__(self, *args, **kwargs):
        perm = self.perm_class(*args, **kwargs)
        return self.operator_type(perm)


class OperandHAndler(OperationHolderMixin):
    def __init__(self, operation_type, perm1, perm2):
        self.operation_type = operation_type
        self.perm1_class = perm1
        self.perm2_class = perm2

    def __call__(self, *args, **kwargs):
        perm1 = self.perm1_class(*args, **kwargs)
        perm2 = self.perm2_class(*args, **kwargs)
        return self.operation_type(perm1, perm2)

    # def check(self, request, user, *args, **kwargs):
    #     operation = self.operation_type(self.perm1, self.perm2)
    #     operation.check(request, user)


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


class NOT:
    def __init__(self, perm):
        self.perm = perm

    def check(self, request, user):
        return not self.perm.check(request, user)


class BasePermissionMetaclass(OperationHolderMixin, type):
    pass


class BasePermission(metaclass=BasePermissionMetaclass):
    def check(self, request, user):
        return True


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


class IsEmailStartsWithA(BasePermission):

    @staticmethod
    def check(request, user):
        return user.email.startswith('a')
