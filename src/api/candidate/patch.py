

from src.apps.candidate.schemas.candidate import CandidatePatchSchema, CandidateSchema
from src.apps.candidate.services.crud import crud_instance
from ninja.errors import ValidationError


async def handler(request, payload: CandidatePatchSchema):
    instance_id = payload.id
    candidate = await crud_instance.read(instance_id)

    if not candidate:
        raise ValidationError("Candidate does not exist")

    updated_instance = await crud_instance.update(candidate, payload.dict())
    return updated_instance


response = CandidateSchema