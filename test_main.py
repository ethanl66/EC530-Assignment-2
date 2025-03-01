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
    assert response.json() == {"name": "God", "email": "god@church.com"}

def test_add_user_invalid():
    response = client.post(
        "/users/",
        json = {"name": "God"}
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{"name": "God", "email": "god@church.com"}]