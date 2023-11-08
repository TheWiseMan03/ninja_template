from src.apps.movie.schemas.movie import MovieDetailSchema, IdMovieSchema
from src.apps.candidate.services.crud import crud_instance
from ninja.errors import ValidationError

response = MovieDetailSchema


async def handler(request, payload: IdMovieSchema):
    pass
    # candidate = await crud_instance.read(payload.id)
    # if not candidate:
    #     raise ValidationError("Candidate does not exist")
    # return MovieDetailSchema.from_orm(candidate)
