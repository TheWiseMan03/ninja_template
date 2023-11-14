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
    await sync_to_async(movie.directors.set)(directors)
    await sync_to_async(movie.actors.set)(actors)
    await sync_to_async(movie.genres.set)(genres)    
    movie = await Movie.objects.prefetch_related("directors", "actors", "genres").aget(pk=movie.pk)
    print(movie)
    await movie.asave()

    return 201, movie
