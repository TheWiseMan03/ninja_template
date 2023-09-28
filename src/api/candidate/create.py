from src.apps.candidate.services.crud import crud_instance
from src.apps.candidate.schemas import CandidateSchema, CreateCandidateSchema
from lib.permissions import IsAdmin, ReadOnly, IsNameStartsWithA, IsAuthenticated

response = { 201: CandidateSchema }
permissions = [(IsAuthenticated() & IsNameStartsWithA()) | IsAdmin]

async def handler(request, payload: CreateCandidateSchema):
    instance = await crud_instance.create(payload.dict())
    return 201, instance


