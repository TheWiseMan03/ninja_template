from src.apps.candidate.schemas.candidate import CandidateSchema, IdCandidateSchema
from src.apps.candidate.services.crud import crud_instance
from ninja.errors import ValidationError
from rest_framework.permissions import IsAuthenticated

response = CandidateSchema

permissions = [IsAuthenticated]


async def handler(request, payload: IdCandidateSchema):
    candidate = await crud_instance.read(payload.id)
    if not candidate:
        raise ValidationError("Candidate does not exist")
    return CandidateSchema.from_orm(candidate)
