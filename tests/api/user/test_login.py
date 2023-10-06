import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_login(client, url_name, created_user):

    payload = dict(
        username=created_user.username,
        password=created_user.raw_password,
    )

    url = url_name(__file__)
    response = client.post(url, payload)

    result = response.json()["data"]

    assert response.status_code == 200

    assert result["access"].startswith("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
    assert result["refresh"].startswith("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
