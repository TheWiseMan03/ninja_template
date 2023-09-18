# Create an API

It is necessary to import [crud_instance](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CREATING_CRUD.md), the corresponding schemas.
```bash
from src.apps.your_app_name.crud import crud_instance
...
```

Create an asynchronous function called handler. Do not use a decorator, but we specify the parameters that are usually passed to the decorator in a variable.

**Please familiarize yourself with the logic of creating a [decorator](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/API_HANDLER.md) for a handler.**

The URL will be automatically generated given the path from the root `api/` to your file.
```bash

response = 'your_instance_to_response'
auth = ...


async def handler(request, ...):
    # Add your function logic here.
    ...
```

# Example of using the `create` method from `crud_instance`

```bash
# Import the necessary modules from your applications
from src.apps.your_app_name.crud import crud_instance
from src.apps.your_app_name.schemas import ResponseSchema, CreateSchema

#Create a response dictionary where the key 201 represents the HTTP status and the ResponseSchema value represents the response schema
response = {201, ResponseSchema}


# Define an asynchronous handler function that accepts request and payload data
async def handler(request, payload: CreateSchema):
    # Use crud_instance.create to create a new instance using data from payload
    instance = await crud_instance.create(payload:dict())
    # Return a tuple with HTTP status 201 and a created instance
    return 201, instance
```