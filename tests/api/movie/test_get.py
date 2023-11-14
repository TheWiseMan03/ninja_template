import pytest


@pytest.mark.django_db
def test_get(auth_client, url_name, movie_creation):
    payload = dict(
        id=movie_creation.id,
    )
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    result = response.json()["data"]

    assert response.status_code == 200
    assert result["id"] == payload["id"]
    assert result["title"] == movie_creation.title