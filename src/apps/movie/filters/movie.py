from ninja import Schema
from typing import Optional


class MovieFilter(Schema):
    category_name: Optional[str]
    genre_name: Optional[str]
    ratingstar_id: Optional[int]
