from django.urls import reverse_lazy
import pytest, json

from django.test import Client

from pytest_factoryboy import register
from ddd.urls import URL_NAMESPACE
from tests.factories.candidate import CandidateFactory
from tests.factories.user import UserFactory

from django.contrib.auth.models import User

register(CandidateFactory)
register(UserFactory)



DEFAULT_CONTENT_TYPE = 'application/json'

class APIClient(Client):
    def post(self, path, data=None, content_type=DEFAULT_CONTENT_TYPE, **extra):
        if data and content_type == DEFAULT_CONTENT_TYPE:
            data = json.dumps(data)
        return super().post(path, data, content_type, **extra)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(login):
    return APIClient(
        headers={
            "Authorization": f"Bearer {login['access']}"
        }
    )


@pytest.fixture
def url_name():
    return lambda file_name: reverse_lazy(URL_NAMESPACE + ":" + file_name.partition('tests')[2].replace('/', '.').replace('.py', '').replace('test_', '')[1:])


# @pytest.fixture
# def created_user(user_factory):
#     user_data = user_factory.build()
#     user = User.objects.create_user(username=user_data.username, email=user_data.email, password=user_data.password)
#     user.raw_password = user_data.password
#     user.is_staff = True
#     user.is_superuser = True
#     user.save()
#
#     return user


@pytest.fixture
def created_user(user_factory):
    user_data = user_factory.build()
    user = User.objects.create_user(username='aaa', email='b@gmail.com', password=user_data.password)
    user.raw_password = user_data.password
    user.is_staff = True
    user.is_superuser = True
    user.save()
    return user


@pytest.fixture
def login(client, url_name, created_user):
    payload = dict(
        username=created_user.username,
        password=created_user.raw_password,
    )
    response = client.post("/api/user/login/", payload)

    return response.json()['data']
