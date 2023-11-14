from src.apps.movie.services.crud import crud_instance_movie
from src.apps.movie.schemas.movie import CreateMovieSchema, MovieDetailSchema
from asgiref.sync import sync_to_async
from src.apps.movie.models import Movie


response = {201: MovieDetailSchema}

async def handler(request, data: CreateMovieSchema):
    data = data.dict()
    directors = data.pop("directors_id", [])
    actors = data.pop("actors_id", [])
    genres = data.pop("genres_id", [])

    movie = await crud_instance_movie.create(data)
    await movie.directors.aset(directors)
    await movie.actors.aset(actors)
    await movie.genres.aset(genres)
    await movie.asave()
    movie = await Movie.objects.prefetch_related("directors", "actors", "genres").aget(pk=movie.pk)

    return 201, movie
