import pytest
from django.test import Client
from model_bakery import baker
from django.test import TestCase


def test_admin_home(client: Client):
    resp = client.get('/admin/login/?next=/admin/')
    assert resp.status_code == 200


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user = baker.make(django_user_model, first_name='Vitor')
    return user


def test_user(user):
    TestCase().assertEqual(user.first_name, 'Vitor')
