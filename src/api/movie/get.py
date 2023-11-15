from src.apps.movie.schemas.movie import MovieDetailSchema, IdMovieSchema
from src.apps.movie.services.crud import crud_instance_movie

response = MovieDetailSchema


async def handler(request, payload: IdMovieSchema):
    movie = await crud_instance_movie.read(payload.id)
    
    movie = await crud_instance_movie.read(payload.id, related_fields=["directors", "actors", "genres"])
    
    return movie

