from src.apps.candidate.services.crud import crud_instance
from src.apps.candidate.schemas import CandidateSchema, CreateCandidateSchema
from lib.permissions import IsAdmin, ReadOnly, IsNameStartsWithA, IsAuthenticated, IsEmailStartsWithA

response = { 201: CandidateSchema }
permissions = [IsNameStartsWithA & IsAuthenticated & ~ IsEmailStartsWithA]


async def handler(request, payload: CreateCandidateSchema):
    instance = await crud_instance.create(payload.dict())
    return 201, instance
