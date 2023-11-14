from src.apps.movie.schemas.movie import MovieDetailSchema, IdMovieSchema
from src.apps.movie.services.crud import crud_instance_movie
from src.apps.movie.models import Movie
from ninja.errors import ValidationError

response = MovieDetailSchema


async def handler(request, payload: IdMovieSchema):
    movie = await crud_instance_movie.read(payload.id)
    if not movie:
        raise ValidationError("Movie does not exist")
    
    movie = await crud_instance_movie.read(payload.id, related_fields=["directors", "actors", "genres"])
    
    return MovieDetailSchema.from_orm(movie)

