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
