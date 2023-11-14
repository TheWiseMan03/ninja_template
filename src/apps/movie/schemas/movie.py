from ninja import Schema, ModelSchema
from datetime import date
from typing import Optional, List
from pydantic import validator
from lib.schema import BasePaginatedResponseSchema
from src.apps.movie.models import Movie


class MovieListSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = '__all__'


class CreateMovieSchema(ModelSchema):
    directors_id: List[int]
    actors_id: List[int]
    genres_id: List[int] = None
    category_id: int

    class Config:
        model = Movie
        model_exclude = ("directors", "actors", "genres", "category")


class MoviePatchSchema(ModelSchema):
    directors: List[int] = []
    actors: List[int] = []
    genres: List[int] = []
    category_id: int = None
    class Config:
        model = Movie
        model_exclude = ("directors", "actors", "genres", "category")
        model_fields_optional = "__all__"


class IdMovieSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = ("id",)


class MovieDetailSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = '__all__'



class PaginatedMovieSchema(BasePaginatedResponseSchema):
    items: List[MovieDetailSchema] 
