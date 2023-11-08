import pytest

from src.apps.user.models import CustomUser


@pytest.mark.django_db
def test_login(client, url_name, user_factory):
    payload = dict(
        username=user_factory.username,
        password=user_factory.password)
    
    print(payload)

    url = url_name(__file__)
    response = client.post(url, payload)
    print(response.json())

    result = response.json()["data"]
    

    assert response.status_code == 200

    assert result["access"].startswith("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
    assert result["refresh"].startswith("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
