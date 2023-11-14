from django.urls import reverse_lazy
from src.apps.user.models import CustomUser
import pytest, json

from django.test import Client

from pytest_factoryboy import register
from ddd.urls import URL_NAMESPACE
from tests.factories import (
    CandidateFactory, 
    MovieFactory, 
    RelationFactory,
    ActorFactory,
    )

from src.apps.user.models import CustomUser
from src.apps.movie.models import Category, Actor, Genre, Movie

register(CandidateFactory)
register(RelationFactory)
register(MovieFactory)
register(ActorFactory)


DEFAULT_CONTENT_TYPE = "application/json"


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
    return APIClient(headers={"Authorization": f"Bearer {login['access']}"})


@pytest.fixture
def url_name():
    return lambda file_name: reverse_lazy(
        URL_NAMESPACE
        + ":"
        + file_name.partition("tests")[2]
        .replace("/", ".")
        .replace(".py", "")
        .replace("test_", "")[1:]
    )


@pytest.fixture
def created_user():
    user = CustomUser.objects.create_user(username="test", password="test", email="test@gmail.com")
    user.save()
    
    return user

@pytest.fixture
def login(client, url_name, created_user):
    payload = dict(
        username=created_user.username,
        password="test",
    )
    response = client.post("/api/user/login/", payload)

    return response.json()["data"]

@pytest.fixture
def foreign_keys_handling():
    payload_category = dict(
        name="test_category",
        description="test_description",
        url="test_url"
    )
    payload_actor = dict(
        name="test_actor",
        age = 18,
        description="test_description",
    )
    payload_genre = dict(
        name="test_genre",
        description="test_description",
        url="test_url"
    )
    category = Category.objects.create(**payload_category)
    actor = Actor.objects.create(**payload_actor)
    genre = Genre.objects.create(**payload_genre)
    return category, actor, genre


@pytest.fixture
def movie_creation(foreign_keys_handling):
    category, actor, genre = foreign_keys_handling
    movie = Movie.objects.create(
        title="test",
        tagline="test",
        description="test",
        poster="test",
        year=2020,
        country="test",
        world_premiere="2020-01-01",
        budget=100,
        fees_in_usa=100,
        fess_in_world=100,
        category=category,
        url="test",
        draft=False
    )
    movie.directors.add(actor)
    movie.actors.add(actor)

    movie.genres.add(genre)
    return movie

