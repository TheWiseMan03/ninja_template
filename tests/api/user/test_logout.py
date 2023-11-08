# import pytest


# @pytest.mark.django_db
# def test_logout(client, url_name, login):
#     url = url_name(__file__)

#     payload = dict(
#         refresh=login["refresh"],
#     )

#     header = {"Authorization": f"Bearer {login['access']}"}

#     response = client.post(url, payload, headers=header)

#     assert response.status_code == 204
