import pytest


@pytest.mark.django_db
def test_get(auth_client, url_name, candidate_factory):
    candidate = candidate_factory.create()

    payload = dict(
        id=candidate.id,
    )
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    result = response.json()["data"]

    assert response.status_code == 200
    assert result["id"] == payload["id"]
    assert result["name"] == candidate.name
