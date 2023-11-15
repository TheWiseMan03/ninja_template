from src.apps.movie.schemas.movie import MoviePatchSchema, MovieDetailSchema
from src.apps.movie.services.crud import crud_instance_movie

response = MovieDetailSchema

# async def handler(request, payload: MoviePatchSchema):
#     movie = await crud_instance_movie.read(payload.id)

#     if not movie:
#         raise ValidationError("Movie does not exist")

#     data = payload.dict(exclude_unset=True)
#     if 'actors' in data:
#         await movie.actors.aset(data.pop('actors'))
#     if 'directors' in data:
#         await movie.directors.aset(data.pop('directors'))
#     if 'genres' in data:
#         await movie.genres.aset(data.pop('genres'))
#     updated_instance = await crud_instance_movie.update(movie, data)
#     instance = await crud_instance_movie.read(updated_instance.id, related_fields=["directors", "actors", "genres"])
#     return instance

async def handler(request, payload: MoviePatchSchema):
    movie = await crud_instance_movie.read(payload.id)

    data = payload.dict(exclude_unset=True)
    related_fields = ['actors', 'directors', 'genres']
    for field in related_fields:
        if field in data:
            await getattr(movie, field).aset(data.pop(field))
    updated_instance = await crud_instance_movie.update(movie, data)
    instance = await crud_instance_movie.read(updated_instance.id, related_fields=related_fields)
    return instance