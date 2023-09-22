# Running the App

Follow these steps to run the Django app on your local machine:

## Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Virtual environment

## Setup

1. Clone the repository:
```bash
git clone git@git.unicon.uz:j.rabbimov/django-ninja-template.git  
cd django-ninja-template
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Database Setup

1. Run migrations:
```bash
python manage.py migrate
```

## Running the App

1. Start the development server:
```bash
python manage.py runserver
```

## Running tests
1. Run tests

```bash
pytest
```

## Documentation reading steps:

1. [CODE_OF_CONDUCT.md](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/CODE_OF_CONDUCT.md)
2. [PROJECT_STRUCTURE.md](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/PROJECT_STRUCTURE.md)
3. [API_CONTROLLER.md](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/API_CONTROLLER.md)
4. [TESTS_STRUCTURE.md](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/TESTS_STRUCTURE.md)
5. [AUTH_INTEGRATION.md](https://git.unicon.uz/j.rabbimov/django-ninja-template/-/blob/docs/docs/AUTH_INTEGRATION.md)