import factory

from tests.faker import fake

from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.name()
    password = fake.password()
    email = fake.email()
