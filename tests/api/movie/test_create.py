import pytest


@pytest.mark.django_db
def test_create(auth_client, url_name, foreign_keys_handling):
    category, actor, genre = foreign_keys_handling
    payload = dict(
        title="test",
        tagline="test",
        description="test",
        poster="test",
        year=2020,
        country="test",
        directors_id=[actor.id],
        actors_id=[actor.id],
        genres_id=[genre.id],
        world_premiere="2020-01-01",
        budget=100,
        fees_in_usa=100,
        fess_in_world=100,
        category_id=category.id,
        url="test",
        draft=False
    )
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    assert response.status_code == 201