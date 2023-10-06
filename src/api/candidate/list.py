from lib.paginator import paginate_response
from src.apps.candidate.filters.candidate import CandidateFilter
from src.apps.candidate.schemas.candidate import (
    CandidateSchema,
    PaginatedCandidateSchema,
)
from src.apps.candidate.services.crud import crud_instance

from src.apps.candidate.permissions import IsAdminUser, IsStaffUser

from ninja import Query

response = PaginatedCandidateSchema
permissions = [IsAdminUser & IsStaffUser]


async def handler(
    request,
    filters: CandidateFilter = Query(...),
    page: int = 1,
    size: int = 10,
):
    filter_args = filters.dict(exclude_unset=True)

    qs = crud_instance.Model.objects.filter(**filter_args)

    return await paginate_response(qs, CandidateSchema, page, size)

    # return await crud_instance.get_list()
