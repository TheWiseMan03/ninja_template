# import pytest


# @pytest.mark.django_db
# def test_delete(auth_client, url_name, candidate_factory):
#     candidate = candidate_factory.create()

#     payload = dict(
#         id=candidate.id,
#     )
#     url = url_name(__file__)

#     response = auth_client.post(url, payload)

#     assert response.status_code == 204

#     with pytest.raises(candidate.DoesNotExist):
#         candidate.refresh_from_db()
