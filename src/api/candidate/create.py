from src.apps.candidate.services.crud import crud_instance
from src.apps.candidate.schemas import CandidateSchema, CreateCandidateSchema
from rest_framework.permissions import IsAdminUser, IsAuthenticated

response = { 201: CandidateSchema }
permissions = [IsAuthenticated ]


async def handler(request, payload: CreateCandidateSchema):
    instance = await crud_instance.create(payload.dict())
    return 201, instance
