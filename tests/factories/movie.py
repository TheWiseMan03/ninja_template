import factory
from tests.faker import fake
from src.apps.movie.models import Movie, Actor, Genre, Category
import uuid


class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    name = fake.name()
    age = fake.pyint()
    description = fake.text()

class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    name = fake.name()
    age = fake.pyint()
    description = fake.text()

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = fake.name()
    description = fake.text()
    url = factory.Sequence(lambda n: f'url{n}')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = "Action"
    description = fake.text()
    url = factory.Sequence(lambda n: f'url{n}')


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie
        skip_postgeneration_save = True

    title = fake.name()
    tagline = fake.text(max_nb_chars=80)
    description = fake.text()
    poster = fake.image_url()
    year = fake.year()
    country = fake.country()
    world_premiere = fake.date()
    budget = fake.pyint()
    fees_in_usa = fake.pyint()
    fess_in_world = fake.pyint()
    category = factory.SubFactory(CategoryFactory)
    url = factory.Sequence(lambda n: f'url{n}')
    draft = False

    @factory.post_generation
    def directors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for director in extracted:
                self.directors.add(director)
        else:
            self.directors.add(DirectorFactory())

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for actor in extracted:
                self.actors.add(actor)
        else:
            self.actors.add(ActorFactory())

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genres.add(genre)
        else:
            self.genres.add(GenreFactory())
