import pytest
import json
from user import User
from house import House
from room import Room
from device import Device

def print_file(file_path):
    """Prints the contents of a file to the console."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# User class --------------------------------------------------------

# Create a user
def test_create_user():
    user1 = User(1, 'John Doe', 'johndoe', '123-555-7890', 'johndoe@mail.com')
    assert user1.id == 1
    assert user1.name == 'John Doe'
    assert user1.username == 'johndoe'
    assert user1.phone == '123-555-7890'
    assert user1.email == 'johndoe@mail.com'

def test_create_user():
    user2 = User(2, 'Jane Doe', 'janedoe', '123-555-7891', 'janedoe@mail.com')
    assert user2.id == 2
    assert user2.name == 'Jane Doe'
    assert user2.username == 'janedoe'
    assert user2.phone == '123-555-7891'
    assert user2.email == 'janedoe@mail.com'

def test_save_user(tmpdir):
    # Create a user
    user = User(10, 'Johnny Doe', 'johnnydoe', '127-555-7890', 'johnydoe@mail.com')
    
    # Save the user
    user.save_user()

    # Verify that the user has been saved correctly
    with open('data/users.json', 'r') as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]['id'] == 10
        assert data[0]['name'] == 'Johnny Doe'
        assert data[0]['username'] == 'johnnydoe'
        assert data[0]['phone'] == '124-555-7890'
        assert data[0]['email'] == 'johnnydoe@mail.com'

user1 = User(1, 'John Doe', 'johndoe', '123-555-7890', 'johndoe@mail.com')
user2 = User(2, 'Jane Doe', 'janedoe', '123-555-7891', 'janedoe@mail.com')
user2.save_user()
print_file('data/users.json')
print()

# Delete a user
user1.delete_user()
print_file('data/users.json')
print()

# Read
print(user2.get_details())

# Update
user2.update_user(name = 'Johnny Smither', username = 'johnnysmither')
print(user2.get_details())

# Load
user3 = User(3, 'Kim Hyung', 'kimmy', '321-555-7890', 'kimhyung@mail.com')
print(user3.get_details())
user3.load_user(2)
print(user3.get_details())


# House class --------------------------------------------------------
# Create a house
house1 = House(1, 'House of John Doe', '123 Main St.', '123.456, 789.012', 1 , 1)
house2 = House(2, 'House of Jane Doe', '456 Elm St.', '456.789, 012.345', 2, [1, 2])
house1.save_house()
house2.save_house()
print_file('data/houses.json')
print()

# Delete a house
house2.delete_house()
print_file('data/houses.json')
print()

# Update and Read
house1.update_house(name = 'Mansion of John Doe', address = '42 Cummington Mall')
print(house1.get_details())

# Load
house2 = House(2, 'New House of Jane Doe', '789 Oak St.', '789.012, 345.678', 3, [1, 2])
print(house2.get_details())
house2.load_house(1)
print(house2.get_details())


# User and House class --------------------------------------------------------
# Add house to user
user1.add_house(house1)
print(user1.get_details())

# Delete house from user
user1.delete_house(1)
print(user1.get_details())


# Room class --------------------------------------------------------
# Create a room
room1 = Room(1, 'Living Room John Doe', 1, 200, (10, 20), 'Living Room', 1)
room2 = Room(2, 'Kitchen John Doe', 1, 150, (10, 15), 'Kitchen', 1)
room1.save_room()
room2.save_room()
print_file('data/rooms.json')
print()

# Delete a room
room2.delete_room()
print_file('data/rooms.json')
print()

# Update and Read
room1.update_room(name = 'Basement of John Doe', floor = 0, size = 300, dimensions = (15, 20), room_type = 'Basement')
print(room1.get_details())

# Load
room2 = Room(2, 'New Kitchen John Doe', 1, 150, (10, 15), 'Kitchen', 1)
print(room2.get_details())
room2.load_room(1)
print(room2.get_details())

# House and Room class --------------------------------------------------------
# Add room to house
house1.add_room(room1)
print(house1.get_details())

# Delete room from house
house1.delete_room(1)
print(house1.get_details())
print()


# Device class --------------------------------------------------------
# Create a device
device1 = Device(1, 'Smart Light', 'Light', [room1], {"operational": True, "current_brightness": 0}, {"max_brightness": 70, "color": "white"}, {"lifespan_hours": 50000, "hours_lit": 1252})
device2 = Device(2, 'Smart Thermostat', 'Thermostat', [room1], {"operational": True, "current_temperature": 70}, {"target_temperature": 74, "max_temperature": 85, "min_temperature": 60, "temperature_unit": "Fahrenheit"}, {"past_24hr_temperatures": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]})
device1.save_device()
device2.save_device()
print_file('data/devices.json')
print()

# Delete a device
device2.delete_device()
print_file('data/devices.json')
print()

# Update and Read
device1.update_device(name = 'Smart Light Bulb', device_type = 'Light Bulb', room = [room2], status = {"operational": False, "current_brightness": 0}, settings = {"max_brightness": 70, "color": "white"}, data = {"lifespan_hours": 50000, "hours_lit": 4930})
print(device1.get_details())

# Load
device2 = Device(2, 'New Smart Thermostat', 'Thermostat', [room1], {"operational": True, "current_temperature": 70}, {"target_temperature": 74, "max_temperature": 85, "min_temperature": 60, "temperature_unit": "Fahrenheit"}, {"past_24hr_temperatures": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 89, 86, 82]})
print(device2.get_details())
device2.load_device(1)
print(device2.get_details())
print()

# Room and Device class --------------------------------------------------------
# Add device to room
room1.add_device(device1)
print(room1.get_details())

# Delete device from room
room1.delete_device(device1)
print(room1.get_details())
