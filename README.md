# credcard
Project developed for technical challenge

![Django CI](https://github.com/vitorpvcampos/credcard/workflows/Django%20CI/badge.svg)
[![Updates](https://pyup.io/repos/github/vitorpvcampos/credcard/shield.svg)](https://pyup.io/repos/github/vitorpvcampos/credcard/)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django 3.1.4](https://img.shields.io/badge/django-3.1.4-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/vitorpvcampos/django-e-learning/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/vitorpvcampos/credcard/branch/main/graph/badge.svg?token=TAO5YHJ7I4)](https://codecov.io/gh/vitorpvcampos/credcard)

This project was developed as a requirement of a selective process for a vacancy as a Python Developer. 

The objective was to implement an application that allows the request of a credit card from the user's information, through a Restful API. I used [Django](https://docs.djangoproject.com/en/3.1/)) and [Django REST Framework](https://www.django-rest-framework.org/).

A live demo can be seen at [Heroku](https://credcard-vitor.herokuapp.com/).

As differentials:
* CPF validation
* Containerized Docker application 

## How to run the project?

### Cloning the repository and creating the ```.env``` file
Supposing you have ```git``` and ```python``` >= ```3.9.0``` installed (not tested on older versions):

```
git clone https://github.com/vitorpvcampos/credcard.git
cd credcard
cp contrib/env-sample .env
pip install --upgrade pip
pip install pipenv
pipenv install --dev
```

### Using Docker with Docker Compose and running the migrations:

```
docker-compose build
docker-compose up -d
docker-compose run app python manage.py migrate
docker-compose run app python manage.py createsuperuser
```

#### PEP8 lint
```
pipenv run flake8
```

#### Testing with pytest
```
pipenv run pytest --cov=compemp
```

##### Work environment

The project was developed using an iMac Pro (via ```OpenCore 0.6.3```) running macOS Big Sur version 11.0.1 and the IDE PyCharm Professional 2020.2.3. The implementation was also tested on the Linux distribution POP!_OS 20.10 (running on the same hardware), with the same IDE.

<p align="center">
    <img src="https://sociedadenovoaeon.org/wp-content/uploads/neofetch.png" alt="Bootstrap logo" width="448" height="280">
  </a>
</p>