import factory

from tests.faker import fake

from src.apps.user.models import CustomUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Faker('email')
    username = fake.user_name()
    password = fake.password()
