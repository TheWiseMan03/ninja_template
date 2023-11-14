import pytest


@pytest.mark.django_db
def test_patch(auth_client, url_name, movie_factory, actor_factory):
    movie = movie_factory.create()
    actor = actor_factory.create()

    payload = dict(id=movie.id, title="Titanic", tagline="Some Title Here", actors=[actor.id])
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    result = response.json()["data"]

    movie.refresh_from_db()

    assert response.status_code == 200

    assert result["id"] == movie.id
    assert result["title"] == movie.title
    assert result["tagline"] == movie.tagline
