import pytest
from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

""" ================= Test User CRUD operations ================= """

def test_create_user():
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
    assert response.json() == {
      'id': 1,
      'name': 'God',
      'email': 'god@church.com',
      'houses': [],
    }

def test_update_user(): 
    response = client.put(
        "/users/1",
        json = {"name": "Jesus", "email": "son@church.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Eve",
        "email": "eve@earth.com",
        "houses_ids": [1, 2]
    }

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}

# Add more invalid input cases


""" ================= Test House CRUD operations ================= """

def test_create_house():
    response = client.post(
        "/houses/",
        json = {
            "address": "1 Heaven St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id":1,
        "address":"1 Heaven St.",
        "owner_id":1,
        "residents_ids":[1,2]
    }

def test_get_houses():
    response = client.get("/houses/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id":1,
            "address":"1 Heaven St.",
            "owner_id":1,
            "residents_ids":[1,2]
        }
    ]

def test_get_house_by_id():
    response = client.get("/houses/1")
    assert response.status_code == 200
    assert response.json() == {
        "id":1,
        "address":"1 Heaven St.",
        "owner_id":1,
        "residents_ids":[1,2]
    }

def test_update_house():
    response = client.put(
        "/houses/1",
        json = {
            "address": "1 Heaven St.",
            "owner_id": 2,
            "residents_ids": [2]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "address": "1 Heaven St.",
        "owner_id": 2,
        "residents_ids": [2]
    }

def test_delete_house():
    response = client.delete("/houses/1")
    assert response.status_code == 200
    assert response.json() == {"message": "House deleted successfully"}

# Add more invalid input cases


def test_add_house_to_user():
    response = client.post(
        "/users/1",
        json = {
            "name": "Eve",
            "email": "eve@earth.com",
            "houses_ids": [1, 2]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Eve",
        "email": "eve@earth.com",
        "houses_ids": [1, 2]
    }

def test_get_houses_by_user():
    response = client.get("/users/1/houses")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "address": "1 Heaven St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    ]