from src.apps.movie.schemas.movie import IdMovieSchema
from src.apps.movie.services.crud import crud_instance


async def handler(request, payload: IdMovieSchema):
    pass
    # movie = await crud_instance.read(payload.id)
    # await crud_instance.delete(movie)

    # return 204