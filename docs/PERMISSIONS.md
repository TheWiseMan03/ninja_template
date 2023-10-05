# Permissions

You can chain  as many permissions as you want. Supported operands ~, &, | meaning Not, And, OR respectively.
For example:

`permissions = [perm1 & perm2 ~perm4]` 

First it checks whether perm1 and perm2 both returns True
and then checks if perm4 return False. If first permission returns False
it never checks next permissions thus raising HTTP 403 error.

## Applying custom permissions:
To apply custom permission define a class that inherits from `BasePermission` class from `lib.permissions` module
and override method:
```python
    def has_permission(self, request, user):
         ...
```
To give all access to a user who has admin privileges else read only access
define a permission class like below:

```python
from lib.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, user):
        if request.method == 'GET':
            return True
        return user.is_staff

```

And apply your custom permission:
```python
permissions = [IsAdminOrReadOnly ]

async def handler(request, payload):
    ...
```








