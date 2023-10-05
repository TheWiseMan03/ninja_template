# Permissions

## Applying django-restframework's permissions:
First of all install django-restframework using pip `pip install djangorestframework`.
Add 'rest_framework' to 'INSTALLED_APPS' list in settings.py file.

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
``` 
Right above the handler method declare your permissions like below:
```commandline
from rest_framework.permissions import IsAdminUser, IsAuthenticated

permissions = [IsAuthenticated ]

async def handler(request, payload):
    ...
``` 
Or you can combine multiple permissions:
```commandline
permissions = [IsAuthenticated & IsAdminUser]

```
You can chain  as many permissions as you want. Supported operands ~, &, | meaning Not, And, OR respectively.
For example:

`permissions = [perm1 & perm2 ~ perm4]` 

First it checks whether perm1 and perm2 both returns True
and then checks if perm4 return False. If first permission returns False
it never checks next permissions thus raising HTTP 403 error.

## Applying custom permissions:
To apply custom permission define a class that inherits from `BasePermission` class from `lib.permissions` module
and override method:
```
    def has_permission(self, request, user):
         ...
```
To give all access to a user who has admin privileges else read only access
define a permission class like below:

```commandline
from lib.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, user):
        if request.method == 'GET':
            return True
        return user.is_staff

```

And apply your custom permission:
```commandline
permissions = [IsAdminOrReadOnly ]

async def handler(request, payload):
    ...
```








