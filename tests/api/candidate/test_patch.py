import pytest


@pytest.mark.django_db
def test_patch(auth_client, url_name, candidate_factory):
    candidate = candidate_factory.create()

    payload = dict(
        id=candidate.id,
        name="John",
        surname="Doe",
    )
    url = url_name(__file__)

    response = auth_client.post(url, payload)

    result = response.json()['data']

    candidate.refresh_from_db()

    assert response.status_code == 200

    assert result['id'] == candidate.id
    assert result['name'] == candidate.name
    assert result['surname'] == candidate.surname
