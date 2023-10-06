import factory

from tests.faker import fake

from src.apps.candidate.models import Relation


class RelationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Relation

    name = fake.name()
