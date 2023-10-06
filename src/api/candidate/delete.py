from src.apps.candidate.schemas.candidate import IdCandidateSchema
from src.apps.candidate.services.crud import crud_instance


async def handler(request, payload: IdCandidateSchema):
    candidate = await crud_instance.read(payload.id)
    await crud_instance.delete(candidate)

    return 204, None


response = {204: None}
