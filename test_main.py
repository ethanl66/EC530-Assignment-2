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
        'houses_ids': [],
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
            'houses_ids': [],
        }
    ]

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
      'id': 1,
      'name': 'God',
      'email': 'god@church.com',
      'houses_ids': [],
    }

def test_update_user(): 
    response = client.put(
        "/users/1",
        json = {"name": "Jesus", "email": "son@church.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Jesus',
        'email': 'son@church.com',
        'houses_ids': [],
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
        "id": 1,
        "address": "1 Heaven St.",
        "owner_id": 1,
        "residents_ids": [1,2],
        "rooms_ids": []
    }

def test_get_houses():
    response = client.get("/houses/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "address": "1 Heaven St.",
            "owner_id": 1,
            "residents_ids": [1,2],
            "rooms_ids": []
        }
    ]

def test_get_house_by_id():
    response = client.get("/houses/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "address": "1 Heaven St.",
        "owner_id": 1,
        "residents_ids": [1,2],
        "rooms_ids": []
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
        "residents_ids": [2],
        "rooms_ids": []
    }

def test_delete_house():
    response = client.delete("/houses/1")
    assert response.status_code == 200
    assert response.json() == {"message": "House deleted successfully"}
    

# Add more invalid input cases


def test_add_house_to_user():

    # Create 2 users and 2 houses
    client.post(
        "/users/",
        json = {"name": "Adam", "email": "adam@earth.com"}
    )
    client.post(
        "/users/",
        json = {"name": "Eve", "email": "eve@earth.com"}
    )
    client.post(
        "/houses/",
        json = {
            "address": "1 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )
    client.post(
        "/houses/",
        json = {
            "address": "2 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )


    response = client.put(
        "/users/1",
        json = {
            "name": "Adam2",
            "email": "adam2@earth.com",
            "houses_ids": [1, 2]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Adam2",
        "email": "adam2@earth.com",
        "houses_ids": [1, 2]
    }

def test_get_houses_by_user():
    response = client.get("/users/1/houses")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "address": "1 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2],
            "rooms_ids": []
        },
        {
            "id": 2,
            "address": "2 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2],
            "rooms_ids": []
        }
    ]
def test_get_houses_by_poor_user():
    response = client.get("/users/2/houses")
    assert response.status_code == 200
    assert response.json() == []

def test_delete_all():
    response = client.delete("/users/")
    assert response.status_code == 200
    assert response.json() == {"message": "All users deleted successfully"}
    response = client.delete("/houses/")
    assert response.status_code == 200
    assert response.json() == {"message": "All houses deleted successfully"}



""" ================= Test Room CRUD operations ================= """

def test_create_room():

    # A room must first need a house, and a house must first need an owner user
    client.post(
        "/users/",
        json = {"name": "Adam", "email": "adam@earth.com"}
    )
    client.post(
        "/users/",
        json = {"name": "Eve", "email": "eve@earth.com"}
    )
    client.post(
        "/houses/",
        json = {
            "address": "1 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )

    response = client.post(
        "/rooms/",
        json = {
            "name": "Living Room",
            "house_id": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Living Room",
        "house_id": 1,
        "devices_ids": []
    }

    # House must also have a room now
    response = client.get("/houses/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "address": "1 Earth St.",
        "owner_id": 1,
        "residents_ids": [1, 2],
        "rooms_ids": [1]
    }

def test_get_rooms():
    response = client.get("/rooms/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Living Room",
            "house_id": 1,
            "devices_ids": []
        }
    ]

def test_get_room_by_id():
    response = client.get("/rooms/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Living Room",
        "house_id": 1,
        "devices_ids": []
    }

def test_update_room():
    response = client.put(
        "/rooms/1",
        json = {
            "name": "Laundry Room",
            "house_id": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Laundry Room",
        "house_id": 1,
        'devices_ids': [],
    }

def test_get_rooms_by_house():
    response = client.get("/houses/1/rooms")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Laundry Room",
            "house_id": 1,
            "devices_ids": []
        }
    ]

def test_delete_room():
    response = client.delete("/rooms/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Room deleted successfully"}

    # Check room deleted from house
    response = client.get("/houses/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "address": "1 Earth St.",
        "owner_id": 1,
        "residents_ids": [1, 2],
        "rooms_ids": []
    }

    response = client.get("/rooms/")
    assert response.status_code == 200
    assert response.json() == []

def test_delete_all():
    response = client.delete("/users/")
    assert response.status_code == 200
    assert response.json() == {"message": "All users deleted successfully"}
    response = client.delete("/houses/")
    assert response.status_code == 200
    assert response.json() == {"message": "All houses deleted successfully"}
    response = client.delete("/rooms/")
    assert response.status_code == 200
    assert response.json() == {"message": "All rooms deleted successfully"}


""" ================= Test Device CRUD operations ================= """
def test_create_device():

    # A device must first need a room, which must first need a house, and a house must first need an owner user
    client.post(
        "/users/",
        json = {"name": "Adam", "email": "adam@earth.com"}
    )
    client.post(
        "/users/",
        json = {"name": "Eve", "email": "eve@earth.com"}
    )
    client.post(
        "/houses/",
        json = {
            "address": "1 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )
    client.post(
        "/houses/",
        json = {
            "address": "2 Earth St.",
            "owner_id": 1,
            "residents_ids": [1, 2]
        }
    )
    client.post(
        "/rooms/",
        json = {
            "name": "Bedroom",
            "house_id": 1
        }
    )
    client.post(
        "/rooms/",
        json = {
            "name": "Kitchen",
            "house_id": 1
        }
    )
    client.post(
        "/rooms/",
        json = {
            "name": "Basement",
            "house_id": 1
        }
    )

    response = client.post(
        "/devices/",
        json = {
            "name": "Bedroom Light",
            "type": "Smart Light",
            "status": {
                "power": True,
                "timer_on": False,
                "timer_left": 600
                       },
            "settings": {
                "color": "white",
                "brightness": 100,
                },
            "data": {
                "hours_on": 5,
                "lifespan": 10000
                },
            "rooms_ids": [1]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Bedroom Light",
        "type": "Smart Light",
        "status": {
            "power": True,
            "timer_on": False,
            "timer_left": 600
        },
        "settings": {
            "color": "white",
            "brightness": 100,
        },
        "data": {
            "hours_on": 5,
            "lifespan": 10000
        },
        "rooms_ids": [1]
    }

    # Room must also have a device now
    response = client.get("/rooms/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Bedroom",
        "house_id": 1,
        "devices_ids": [1]
    }


def test_get_devices():
    response = client.get("/devices/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Bedroom Light",
            "type": "Smart Light",
            "status": {
                "power": True,
                "timer_on": False,
                "timer_left": 600
            },
            "settings": {
                "color": "white",
                "brightness": 100,
            },
            "data": {
                "hours_on": 5,
                "lifespan": 10000
            },
            "rooms_ids": [1]
        }
    ]

def test_get_device_by_id():
    response = client.get("/devices/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Bedroom Light",
        "type": "Smart Light",
        "status": {
            "power": True,
            "timer_on": False,
            "timer_left": 600
        },
        "settings": {
            "color": "white",
            "brightness": 100,
        },
        "data": {
            "hours_on": 5,
            "lifespan": 10000
        },
        "rooms_ids": [1]
    }

def test_update_device():
    response = client.put(
        "/devices/1",
        json = {
            "name": "Bedroom Light",
            "type": "Smart Light",
            "status": {
                "power": False,
                "timer_on": False,
                "timer_left": 600
            },
            "settings": {
                "color": "white",
                "brightness": 100,
            },
            "data": {
                "hours_on": 5,
                "lifespan": 10000
            },
            "rooms_ids": [1]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Bedroom Light",
        "type": "Smart Light",
        "status": {
            "power": 0,
            "timer_on": 0,
            "timer_left": 600
        },
        "settings": {
            "color": "white",
            "brightness": 100,
        },
        "data": {
            "hours_on": 5,
            "lifespan": 10000
        },
        "rooms_ids": [1]
    }

def test_get_device_by_room():
    response = client.get("/rooms/1/devices")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Bedroom Light",
            "type": "Smart Light",
            "status": {
                "power": False,
                "timer_on": False,
                "timer_left": 600
            },
            "settings": {
                "color": "white",
                "brightness": 100,
            },
            "data": {
                "hours_on": 5,
                "lifespan": 10000
            },
            "rooms_ids": [1]
        }
    ]

def test_get_devices_by_house():
    response = client.get("/houses/1/devices")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Bedroom Light",
            "type": "Smart Light",
            "status": {
                "power": False,
                "timer_on": False,
                "timer_left": 600
            },
            "settings": {
                "color": "white",
                "brightness": 100,
            },
            "data": {
                "hours_on": 5,
                "lifespan": 10000
            },
            "rooms_ids": [1]
        }
    ]

def test_delete_device():
    response = client.delete("/devices/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Device deleted successfully"}

    # Check device deleted from room
    response = client.get("/rooms/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Bedroom",
        "house_id": 1,
        "devices_ids": []
    }