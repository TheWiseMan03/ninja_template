from asgiref.sync import sync_to_async


class CRUD_Queryset:
    def __init__(self, Model):
        self.Model = Model

    async def read(self, pk: int, related_fields=None):
        if related_fields:
            return await self.Model.objects.prefetch_related(*related_fields).aget(pk=pk)
        else:
            return await self.Model.objects.aget(pk=pk)

    async def get_list(self, conditions: dict = {}, related_fields=None):
        if related_fields:
            return await sync_to_async(self.Model.objects.filter(**conditions).prefetch_related(*related_fields).all)()
        else:
            return await sync_to_async(self.Model.objects.filter(**conditions).all)()

    async def create(self, data_dict: dict = {}):
        return await self.Model.objects.acreate(**data_dict)

    async def update(self, instance, data_dict: dict = {}):
        for attr, value in data_dict.items():
            setattr(instance, attr, value)
            await instance.asave()
        return instance


    async def delete(self, instance):
        await instance.adelete()
        return instance