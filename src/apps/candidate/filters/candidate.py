from ninja import Schema
from enum import Enum
from typing import Optional


class CandidateTypeEnum(str, Enum):
    P = "P"
    S = "S"
    T = "T"


class CandidateFilter(Schema):
    name__icontains: str = None
    surname__icontains: str = None
    c_type: CandidateTypeEnum = None
