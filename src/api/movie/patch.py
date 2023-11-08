from src.apps.movie.schemas.movie import MoviePatchSchema, MovieDetailSchema
from src.apps.movie.services.crud import crud_instance
from ninja.errors import ValidationError


async def handler(request, payload: MoviePatchSchema):
    pass
#     instance_id = payload.id
#     movie = await crud_instance.read(instance_id)

#     if not movie:
#         raise ValidationError("Candidate does not exist")

#     updated_instance = await crud_instance.update(movie, payload.dict())
#     return updated_instance


# response = MovieDetailSchema