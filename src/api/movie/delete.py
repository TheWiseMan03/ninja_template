from src.apps.movie.schemas.movie import IdMovieSchema
from src.apps.movie.services.crud import crud_instance_movie


response = {204: None}

async def handler(request, payload: IdMovieSchema):
    movie = await crud_instance_movie.read(payload.id)
    await crud_instance_movie.delete(movie)

    return 204, None
