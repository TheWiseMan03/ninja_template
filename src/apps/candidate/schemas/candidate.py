from ninja import ModelSchema, Field
from lib.schema import BasePaginatedResponseSchema
from typing import List

from src.apps.candidate.models import Candidate


class CandidateSchema(ModelSchema):
    class Config:
        model = Candidate
        model_fields = "__all__"


class CandidatePatchSchema(ModelSchema):
    id: int
    relation_id: int

    class Config:
        model = Candidate
        model_exclude = (
            "relation",
        )  # always exclude foreign key field to prevent error, use addition in key name "_id"
        model_fields_optional = "__all__"


class CreateCandidateSchema(ModelSchema):
    class Config:
        model = Candidate
        model_fields = ("name", "surname")


class IdCandidateSchema(ModelSchema):
    class Config:
        model = Candidate
        model_fields = ("id",)


class PaginatedCandidateSchema(BasePaginatedResponseSchema):
    items: List[CandidateSchema]
