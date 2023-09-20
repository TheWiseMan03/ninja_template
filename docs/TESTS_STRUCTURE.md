# Tests Structure

:file_folder: tests

- :open_file_folder: tests
    - :open_file_folder: api
        - :open_file_folder: candidate
            - `test_create.py`
            - `test_delete.py`
            - `test_get.py`
            - `test_list.py`
            - `test_patch.py`
        - :open_file_folder: user
            - `test_login.py`
            - `test_logout.py`
    - :open_file_folder: factories
        - `candidate.py`
        - `user.py`
    <!-- - :open_file_folder: fixtures
        - `auth.py`
        - `candidate.py` -->
    - `conftest.py`
    - `faker.py`

**tests** is used to store modules and files related to testing a software project.

># Note
>
>1. Every test endpoint in your application must be encapsulated in `api/` within that application. As given in **Tests Structure**
>
>2. The conftest.py file defines ready-made fixtures that can be used in your test endpoints.
>
>3. Since you can use the factory library to create and configure the data, which avoids re-declaring the data for each test, it makes working with data in the database easier. An example of using the factory library can be found at this  [`factory`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/tests/factories/candidate.py).
>
>In addition, [`automatic generation of URLs`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/tests/conftest.py#L41) for your tests is implemented, taking into account the path to the test file.



### Below is an example:
```bash
import pytest

@pytest.mark.django_db
def test(auth_client, url_name):

    url = url_name(__file__)

    response = auth_client.get(url)
    ...
```

[`auth_client`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/tests/conftest.py#L32) and [`url_name`](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/tests/conftest.py#L41) are ready-made fixtures. `auth_client` provides authorization-based requests, allowing requests to be made on behalf of an authenticated user. While `url_name` is used to generate URLs based on the path to the current tests file.

In other words, auth_client provides authentication when making requests, and `url_name` makes it easy to create URLs given the current context of the file structure.
