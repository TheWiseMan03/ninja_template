from lib.paginator import paginate_response
from src.apps.movie.filters.movie import MovieFilter
from src.apps.movie.schemas.movie import (
    MovieListSchema,
    PaginatedMovieSchema,
)
from src.apps.movie.services.crud import crud_instance_movie

from src.apps.movie.permissions import IsStaffUser

from ninja import Query

response = PaginatedMovieSchema
permissions = [IsStaffUser]

async def handler(
    request,
    filters: MovieFilter = Query(...),
    page: int = 1,
    size: int = 10,
):
    """
    movie list api
    
    """
    filter_args = filters.dict(exclude_unset=True)

    qs = await crud_instance_movie.get_list(**filter_args)

    return await paginate_response(qs, MovieListSchema, page, size)
