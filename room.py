import json
import os
from validation import *

class Room:
    # Create
    def __init__(self, room_id, name, floor, size, dimensions, room_type, house, devices = []):
        if not isValidID(room_id):
            raise ValueError("Invalid room ID")
        if not isValidNameRoom(name):
            raise ValueError("Invalid name: Must be a string of 1 to 50 characters.")
        if not isValidFloor(floor):
            raise ValueError("Invalid floor: Must be an integer between 0 and 3000.")
        if not isValidSize(size):
            raise ValueError("Invalid size: Must be a positive number.")
        if not isValidDimensions(dimensions):
            raise ValueError("Invalid dimensions: Must be a tuple of 2 positive numbers.")
        if not isValidRoomType(room_type):
            raise ValueError("Invalid room type: Must be a string of 1 to 50 characters.")
        self.room_id = room_id
        self.name = name
        self.floor = floor
        self.size = size
        self.dimensions = tuple(dimensions)
        self.room_type = room_type
        self.house = house
        if devices is not None:
            self.devices = devices

    # Save room to .json file 
    def save_room(self):
        file_path = 'data/rooms.json'
        room_data = self.get_details()

        # Ensure the "data" directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Initialize an empty list if the file doesn't exist or is empty/invalid
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            rooms = []
        else:
            try:
                with open(file_path, 'r') as file:
                    rooms = json.load(file)
            except json.JSONDecodeError:
                # If the file contains invalid JSON, initialize an empty list
                rooms = []

        # Check if the room already exists and update their data
        room_found = False
        for room in rooms:
            if room['room_id'] == self.room_id:
                room.update(room_data)
                room_found = True
                break

        # If the room doesn't exist, append their data
        if not room_found:
            rooms.append(room_data)

        # Write the updated list of rooms back to the file
        with open(file_path, 'w') as file:
            json.dump(rooms, file, indent=4)

    # Load house from .json file
    def load_room(self, room_id):
        file_path = 'data/rooms.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                rooms = json.load(file)
        else:
            return "Room not found"

        for room in rooms:
            if room['room_id'] == room_id:
                self.room_id = room['room_id']
                self.name = room['name']
                self.floor = room['floor']
                self.size = room['size']
                self.dimensions = room['dimensions']
                self.room_type = room['room_type']
                if 'house' in room:
                    self.house = room['house']
                if 'devices' in room:
                    self.devices = room['devices']
                break
        else:
            return "House not found"

    # Assign (Rooms can have multiple devices but can only belong to 1 house)
    def add_device(self, device):
        self.devices.append(device)
        self.save_room()

    def delete_device(self, device):
        for existing_device in self.devices:
            if existing_device.device_id == device.device_id:
                self.devices.remove(device)
                break
        self.save_room()

    # Read
    def get_details(self):
        return {
            'room_id': self.room_id,
            'name': self.name,
            'floor': self.floor,
            'size': self.size,
            'dimensions': self.dimensions,
            'room_type': self.room_type,
            'devices': [device.get_details() for device in self.devices],
            'house': self.house
        }
    
    # Update
    def update_room(self, name = None, floor = None, size = None, dimensions = None, room_type = None):
      
        if name is not None:
            if not isValidNameRoom(name):
                raise ValueError("Invalid name: Must be a string of 1 to 50 characters.")
            self.name = name
        if floor is not None:
            if not isValidFloor(floor):
                raise ValueError("Invalid floor: Must be an integer between 0 and 3000.")
            self.floor = floor
        if size is not None:
            if not isValidSize(size):
                raise ValueError("Invalid size: Must be a positive number.")
            self.size = size
        if dimensions is not None:
            if not isValidDimensions(dimensions):
                raise ValueError("Invalid dimensions: Must be a tuple of 2 positive numbers.")
            self.dimensions = tuple(dimensions)
        if room_type is not None:
            if not isValidRoomType(room_type):
                raise ValueError("Invalid room type: Must be a string of 1 to 50 characters.")
            self.room_type = room_type
        self.save_room()

    # Delete
    def delete_room(self):
        file_path = 'data/rooms.json'

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as file:
            rooms = json.load(file)

        rooms = [room for room in rooms if room['room_id'] != self.room_id]

        with open(file_path, 'w') as file:
            json.dump(rooms, file, indent=4)

    # Search for rooms?
    