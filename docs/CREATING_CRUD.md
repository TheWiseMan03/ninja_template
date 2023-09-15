# An example of creating CRUD operations (Create, Read, Update, Delete) using the [CRUD_Queryset](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CRUD_Queryset.md) class

1. Import `CRUD_Queryset` from `lib.crud`:


```bash
from lib.crud import CRUD_Queryset
```

2. Then import the `model` you want to work with from your application:


```bash
from src.apps.your_app.models import YourModel
```

3. Create an instance of the `CRUD_Queryset` class, passing your model as an argument:


```bash
instance = CRUD_Queryset(YourModel)
```

You now have a crud_instance that can be used to perform CRUD operations on YourModel model objects.

### Please consider an example of using CRUD [CREATING_API](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CREATING_API.md)