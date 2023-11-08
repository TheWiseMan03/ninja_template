from src.apps.movie.schemas.movie import CreateMovieSchema


async def handler(request, data: CreateMovieSchema):
    pass
    # movie = await crud_instance.create(**data.dict())
    # return movie