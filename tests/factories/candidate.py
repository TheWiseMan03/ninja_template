import factory

from tests.faker import fake

from src.apps.candidate.models import Candidate


class CandidateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Candidate

    name = fake.name()
    surname = fake.name()
