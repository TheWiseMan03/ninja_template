# CRUD_Queryset

This class provides a unified interface for performing CRUD operations on a Django model, making the code more readable and maintainable. The class also uses async methods to perform these operations asynchronously, which can be useful when working with asynchronous Django-based applications.

```bash
from asgiref.sync import sync_to_async

class CRUD_Queryset:
    """
    A class for performing CRUD operations on Django model objects using asynchronous methods.
    """

    def __init__(self, Model):
        """
        Initializing the CRUD_Queryset class with Model.
        """
        self.Model = Model

    async def read(self, pk: int):
        """
        Asynchronous method for reading a model object by its primary key (pk).
        """
        return await self.Model.objects.get(pk=pk)

    async def get_list(self, conditions: dict = {}):
        """
        Asynchronous method for obtaining a list of model objects based on specified conditions.
        """
        return await sync_to_async(list)(self.Model.objects.filter(**conditions))

    async def create(self, data_dict: dict = {}):
        """
        An asynchronous method for creating a new model object based on the provided data.
        """
        return await self.Model.objects.create(**data_dict)
    
    async def update(self, instance, data_dict: dict = {}):
        """
        An asynchronous method for updating the attributes of a model object based on supplied data.
        """
        for attr, value in data_dict.items():
            setattr(instance, attr, value)
        await instance.save()
        return instance
    
    async def delete(self, instance):
        """
        Asynchronous method for deleting a model object.
        """
        await instance.delete()
        return instance
```

