from asgiref.sync import sync_to_async


# class CRUD_Queryset:
#     def __init__(self, Model):
#         self.Model = Model

#     async def read(self, pk: int):
#         return await self.Model.objects.aget(pk=pk)

#     async def get_list(self, conditions: dict = {}):
#         return await sync_to_async(self.Model.objects.filter)(**conditions)

#     async def create(self, data_dict: dict = {}):
#         return await self.Model.objects.acreate(**data_dict)

#     async def update(self, instance, data_dict: dict = {}):
#         for attr, value in data_dict.items():
#             setattr(instance, attr, value)
#         await instance.asave()
#         return instance

#     async def delete(self, instance):
#         await instance.adelete()
#         return instance

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
        m2m_fields = ['directors', 'actors', 'genres']
        for attr, value in data_dict.items():
            # if attr in m2m_fields:
            #     m2m_attr = getattr(instance, attr)
            #     await m2m_attr.aset(value)
            #     instance = await self.Model.objects.filter(id=instance.id).prefetch_related(attr).afirst()
            # else:
            setattr(instance, attr, value)

            await instance.asave()
        return instance


    async def delete(self, instance):
        await instance.adelete()
        return instance

    async def update_m2m(self, instance, m2m_field: str, new_values: list):
        m2m_attr = getattr(instance, m2m_field)
        await sync_to_async(m2m_attr.set)(new_values)
        instance = await sync_to_async(self.Model.objects.filter(id=instance.id).prefetch_related(m2m_field).first)()
        await instance.asave()

