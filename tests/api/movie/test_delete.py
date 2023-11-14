import pytest


@pytest.mark.django_db
def test_delete(auth_client, url_name, movie_creation):
    movie = movie_creation

    payload = dict(
        id=movie.id,
    )
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    assert response.status_code == 204
