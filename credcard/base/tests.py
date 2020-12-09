from django.test import Client


def test_admin_home(client: Client):
    resp = client.get('/admin/login/?next=/admin/')
    assert resp.status_code == 200
