

from lib.crud import CRUD_Queryset

from src.apps.candidate.models import Candidate

crud_instance = CRUD_Queryset(Candidate)


