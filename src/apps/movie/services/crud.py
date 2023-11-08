from lib.crud import CRUD_Queryset

from src.apps.movie.models import movie

crud_instance = CRUD_Queryset(movie)
