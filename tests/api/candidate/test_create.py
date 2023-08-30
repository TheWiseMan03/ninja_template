import pytest, json


@pytest.mark.django_db
def test_create(auth_client, url_name):
    payload = dict(
        name="John",
        surname="Doe",
    )

    url = url_name(__file__)

    response = auth_client.post(url, payload)

    result = response.json()['data']

    assert response.status_code == 201

    assert result['name'] == payload['name']
    assert result['surname'] == payload['surname']

