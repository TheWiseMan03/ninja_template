# Code of Conduct

## Features:

>1. Implementation of an authentication mechanism to control user access to project resources.
>2. The ability to record and analyze logs to track actions and events in the application.
>3. A module responsible for handling and managing errors to ensure stable operation of the application.
>4. Custom paginator: Implementation of pagination with the ability to configure parameters for easy navigation through data.
>5. The ability to filter data according to specified criteria or parameters to get more accurate results.
>6. A mechanism for generating URLs based on named routes, making it easier to manage links and navigate between pages

## New files for the application should be organized as follows:

1. The source code of your application is located in the 'src/apps/your_app_name' directory.
2. The API associated with your application is located inside 'src/api/your_app_name'.
3. All API-endpoints should be placed inside '/your_app_api/'.
 

## CRUD Operations
Your application does not need to implement CRUD (Create, Read, Update, Delete) operations for every case. Your application can use ready-made CRUD functionality to work with model objects. To do this you will need to import the `CRUD_Queryset` class from an external library as follows:

```bash
from lib.crud import CRUD_Queryset
```

[CRUD_Queryset](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CRUD_Queryset.md) - provides asynchronous methods for performing basic operations on model objects, enabling efficient data manipulation. This class will perform all CRUD operations for you. You can see an example of constructing CRUD operations at the following link: [CRUD Example](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CREATING_CRUD.md)


## Creating an API

To create an API, you need to create files for each logic in the 'api/your_app_api/' directory. Like that:

1. `create.py` - file for creating data.
2. `update.py` - file for updating data.

...

Each of these files will be responsible for a specific type of data operation in your API.

When creating an API, you must define an asynchronous function called "handler" inside the file, otherwise an error will be generated. There is no need to explicitly create a decorator for this function, as this will be automatically done by the function [`load_api`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/master/lib/controller.py).

Any parameters you want to pass to the decorator can simply be defined in variables with appropriate names and assigned the desired values.

Please see the API creation examples provided at this link: [Create API](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CREATING_API.md)




