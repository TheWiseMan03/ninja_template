from ninja import Schema, ModelSchema
from datetime import date
from typing import Optional, List
from pydantic import validator
from lib.schema import BasePaginatedResponseSchema
from src.apps.movie.models import Movie


class MovieListSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = ("id", "title", "tagline", "category", "poster")


class CreateMovieSchema(ModelSchema):
    directors: List[int]
    actors: List[int]
    genres: List[int]
    category_id: int = None

    class Config:
        model = Movie
        model_exclude = ("directors", "actors", "genres", "category", "draft")
        # model_fields = '__all__'

class MoviePatchSchema(ModelSchema):
    directors: List[int]
    actors: List[int]
    genres: List[int]
    category_id: int = None
    class Config:
        model = Movie
        model_exclude = ("directors", "actors", "genres", "category")
        model_fields_optional = "__all__"


class IdMovieSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = ("id",)


# class MovieListSchema(ModelSchema):
#     id: int
#     title: str
#     tagline: str
#     category: str
#     rating_user: bool
#     middle_star: int
#     poster: str


# class CreateMovieSchema(Schema):
#     id: int
#     title: str
#     tagline: str
#     description: str
#     poster: str
#     year: int
#     country: str
#     directors: List[int]
#     actors: List[int]
#     genres: List[int]
#     world_premiere: date
#     budget: int
#     fees_in_usa: int
#     fess_in_world: int
#     category: int
#     url: str
#     draft: bool


# class ReviewCreateSchema(Schema):
#     email: str
#     name: str
#     text: str
#     parent: Optional[int]


# class ReviewResponseSchema(Schema):
#     name: str
#     text: str
#     parent: Optional[int]
#     movie: str


# class ReviewSchema(Schema):
#     id: int
#     name: str
#     text: str
#     children: List["ReviewSchema"]


# class GenreSchema(Schema):
#     id: int
#     name: str
#     description: str


# class CategorySchema(Schema):
#     id: int
#     name: str
#     description: str


class MovieDetailSchema(Schema):
    class Config:
        model = Movie
        model_exclude = (
            "draft",
        )  # always exclude foreign key field to prevent error, use addition in key name "_id"


class PaginatedMovieSchema(BasePaginatedResponseSchema):
    items: List[MovieDetailSchema] 


# class CreateRatingSchema(Schema):
#     ip: str
#     star_id: int
#     movie_id: int


# class ActorCreateSchema(Schema):
#     name: str
#     age: int
#     description: str
#     image: Optional[str] = None

#     @validator("name", "description", "image")
#     def check_empty(cls, v):
#         if v == "":
#             raise ValueError("Field cannot be empty")
#         return v

#     @validator("age")
#     def check_age(cls, v):
#         if v < 0:
#             raise ValueError("Age cannot be negative")
#         return v

#     @validator("image")
#     def check_image_format(cls, v):
#         valid_image_formats = ["jpg", "jpeg", "png"]
#         if v is not None and v.split(".")[-1] not in valid_image_formats:
#             raise ValueError("Invalid image format")
#         return v
