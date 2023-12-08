import pytest
from main import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_get_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == 200

def test_get_user_by_invalid_id(client):
    response = client.get('/users/999')
    assert response.status_code == 404

def test_create_user(client):
    data = {'name': 'John', 'lastname': 'Doe'}
    response = client.post('/users', json=data)
    assert response.status_code == 201

def test_create_user_invalid_data(client):
    data = {'name': 'John'}
    response = client.post('/users', json=data)
    assert response.status_code == 400

def test_update_user(client):
    data = {'name': 'UpdatedName'}
    response = client.patch('/users/1', json=data)
    assert response.status_code == 204

def test_update_user_invalid_id(client):
    data = {'name': 'UpdatedName'}
    response = client.patch('/users/999', json=data)
    assert response.status_code == 404

def test_replace_user(client):
    data = {'name': 'NewName', 'lastname': 'NewLastname'}
    response = client.put('/users/1', json=data)
    assert response.status_code == 204

def test_replace_user_invalid_id(client):
    data = {'name': 'NewName', 'lastname': 'NewLastname'}
    response = client.put('/users/999', json=data)
    assert response.status_code == 404

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204

def test_delete_user_invalid_id(client):
    response = client.delete('/users/999')
    assert response.status_code == 404
