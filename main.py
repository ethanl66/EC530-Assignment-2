from fastapi import FastAPI, HTTPException
from typing import List
from models import User, House, Room, Device

app = FastAPI()

# In-memory "database"
users_db = []
houses_db = []
rooms_db = []
devices_db = []

""" ========================= USER CRUD OPERATIONS ========================= """
# Get all users
@app.get("/users/", response_model=List[User])
def get_users():
    return users_db

# Get user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Create a new user
@app.post("/users/", response_model=User)
def add_user(user: User):
    user.id = len(users_db) + 1
    users_db.append(user)
    return user

# Update a user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            updated_user.id = user_id
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


""" ================= POSTMAN FOLLOW THIS ==================
in Body, select raw and JSON
{
    "name": "God",
    "email": "god@church.com"
}
"""

""" ================== TERMINAL SEND WITH THIS  ==================
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{
    "name": "God",
    "email": "god@church.com"
}'
"""

""" ========================= HOUSE CRUD OPERATIONS ========================= """
# Get all houses
@app.get("/houses/", response_model=List[House])
def get_houses():
    return houses_db

# Get house by ID
@app.get("/houses/{house_id}", response_model=House)
def get_house(house_id: int):
    for house in houses_db:
        if house.id == house_id:
            return house
    raise HTTPException(status_code=404, detail="House not found")

# Create a new house
@app.post("/houses/", response_model=House)
def add_house(house: House):
    house.id = len(houses_db) + 1
    houses_db.append(house)
    return house

# Update a house
@app.put("/houses/{house_id}", response_model=House)
def update_house(house_id: int, updated_house: House):
    for index, house in enumerate(houses_db):
        if house.id == house_id:
            houses_db[index] = updated_house
            updated_house.id = house_id
            return updated_house
    raise HTTPException(status_code=404, detail="House not found")

# Delete a house
@app.delete("/houses/{house_id}")
def delete_house(house_id: int):
    for index, house in enumerate(houses_db):
        if house.id == house_id:
            houses_db.pop(index)
            return {"message": "House deleted successfully"}
    raise HTTPException(status_code=404, detail="House not found")

# Get houses by user ID
@app.get("/users/{user_id}/houses", response_model=List[House])
def get_houses_by_user(user_id: int):
    user_houses = []
    for house in houses_db:
        if house.owner_id == user_id:
            user_houses.append(house)
    return user_houses


# Make it so that updating a house's owner_id also updates the user's houses_ids
# Make it so that updating a user's houses_ids also updates the house's owner_id

""" ================= POSTMAN FOLLOW THIS ==================
in Body, select raw and JSON
{
    "address": "1 Heaven St.",
    "owner_id": 1,
    "residents_ids": [1, 2]
}
"""

""" ================== TERMINAL SEND WITH THIS  ==================
Invoke-RestMethod -Uri "http://127.0.0.1:8000/houses" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{
    "name": "God",
    "email": "god@church.com"
}'
"""


""" ================= ROOM CRUD OPERATIONS ================= """
# Get all rooms
@app.get("/rooms/")
def get_rooms():
    return rooms_db

# Get room by ID
@app.get("/rooms/{room_id}")
def get_room(room_id: int):
    for room in rooms_db:
        if room.id == room_id:
            return room
    raise HTTPException(status_code=404, detail="Room not found")

# Create a new room
@app.post("/rooms/")
def add_room(room: Room):
    room.id = len(rooms_db) + 1
    rooms_db.append(room)

    # Must also update the house's rooms_ids
    for house in houses_db:
        if house.id == room.house_id:
            house.rooms_ids.append(room.id)
            break

    return room

# Update a room
@app.put("/rooms/{room_id}")
def update_room(room_id: int, updated_room: Room):
    for index, room in enumerate(rooms_db):
        if room.id == room_id:
            rooms_db[index] = updated_room
            updated_room.id = room_id

            # Must also update the house's rooms_ids
            for house in houses_db:
                if house.id == room.house_id:
                    house.rooms_ids.append(room.id)
                    break
                
            return updated_room
    raise HTTPException(status_code=404, detail="Room not found")

# Delete a room
@app.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    for index, room in enumerate(rooms_db):
        if room.id == room_id:
            house_id = room.house_id
            rooms_db.pop(index)

            # Must also update the house's rooms_ids
            for house in houses_db:
                if house_id == house.id:
                    house.rooms_ids.remove(room_id)
                    break
                
            return {"message": "Room deleted successfully"}
    raise HTTPException(status_code=404, detail="Room not found")


# Get rooms by house ID
@app.get("/houses/{house_id}/rooms")
def get_rooms_by_house(house_id: int):
    house_rooms = []
    for room in rooms_db:
        if room.house_id == house_id:
            house_rooms.append(room)
    return house_rooms




""" ================= administrative functions ================= """
# Delete all users
@app.delete("/users/")
def delete_all_users():
    users_db.clear()
    return {"message": "All users deleted successfully"}
# Delete all houses
@app.delete("/houses/")
def delete_all_houses():
    houses_db.clear()
    return {"message": "All houses deleted successfully"}
# Delete all rooms
@app.delete("/rooms/")
def delete_all_rooms():
    rooms_db.clear()
    return {"message": "All rooms deleted successfully"}