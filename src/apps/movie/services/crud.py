from lib.crud import CRUD_Queryset

from src.apps.movie.models import Movie

crud_instance_movie = CRUD_Queryset(Movie)