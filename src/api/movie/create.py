from src.apps.movie.services.crud import crud_instance_movie
from src.apps.movie.schemas.movie import CreateMovieSchema, MovieDetailSchema


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
    movie = await crud_instance_movie.read(movie.pk, related_fields=["directors", "actors", "genres"])


    return 201, movie
