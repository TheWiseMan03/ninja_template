import pytest
from django.urls import reverse_lazy

from ddd.urls import URL_NAMESPACE


@pytest.mark.django_db
def test_list(auth_client, url_name, candidate_factory):
    candidate_factory.create_batch(50)

    url = url_name(__file__)

    response = auth_client.post(url)
    print(response.content)

    result = response.json()["data"]["items"]


    assert response.status_code == 200
    assert len(result) == 10

    sizes = [5, 2, 30, 50]

    for size in sizes:
        paginated_response = auth_client.post(f"{url}?size={size}")
        paginated_result = paginated_response.json()["data"]["items"]
        assert paginated_response.status_code == 200
        assert len(paginated_result) == size
