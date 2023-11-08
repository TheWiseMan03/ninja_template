from ninja import Schema
from enum import Enum
from typing import Optional


class MovieFilter(Schema):
    category_name = str
    genre_name = str
    ratingstar_id = int
