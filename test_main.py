import pytest
from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

# Test User CRUD operations
def test_add_user():
    response = client.post(
        "/users/",
        json = {"name": "God", "email": "god@church.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'God',
        'email': 'god@church.com',
        'houses': [],
    }

def test_add_user_invalid():
    response = client.post(
        "/users/",
        json = {"name": "God"}
    )
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'input': {
                    'name': 'God',
                },
                'loc': [
                    'body',
                    'email',
                ],
                'msg': 'field required',
                'msg': 'Field required',
                'type': 'value_error.missing',
                'type': 'missing',
            },
        ]
    }        
  

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': 1,
            'name': 'God',
            'email': 'god@church.com',
            'houses': [],
        }
    ]

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': 1,
            'name': 'God',
            'email': 'god@church.com',
            'houses': [],
        }
    ]