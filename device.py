import json
import os
from room import Room
from validation import isValidID, isValidNameDevice, isValidDeviceType

class Device:
    # Create
    def __init__(self, device_id, name, device_type, room, status, settings, data):
        if not isValidID(device_id):
            raise ValueError("Invalid device ID")
        if not isValidNameDevice(name):
            raise ValueError("Invalid name")
        if not isValidDeviceType(device_type):
            raise ValueError("Invalid device type")
        
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.room = room if room is not None else []            # can be array of rooms
        self.status = status if status is not None else {}        # can be array of statuses
        self.settings = settings if settings is not None else {}    # can be array of settings
        self.data = data if data is not None else {}           # can be array of data

    # Save device to .json file?
    # If device is not in json file, create a new one. If it is, update the existing one.
    def save_device(self):
        file_path = 'data/devices.json'
        device_data = self.get_details()

        # Ensure the "data" directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Initialize an empty list if the file doesn't exist or is empty/invalid
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            devices = []
        else:
            try:
                with open(file_path, 'r') as file:
                    devices = json.load(file)
            except json.JSONDecodeError:
                # If the file contains invalid JSON, initialize an empty list
                devices = []

        # Check if the device already exists and update their data
        device_found = False
        for device in devices:
            if device['device_id'] == self.device_id:
                device.update(device_data)
                device_found = True
                break

        # If the room doesn't exist, append their data
        if not device_found:
            devices.append(device_data)

        # Write the updated list of rooms back to the file
        with open(file_path, 'w') as file:
            json.dump(devices, file, indent=4)

    # Load device from .json file?
    # If device is not in json file, return an error message. If it is, load the existing one.
    def load_device(self, device_id):
        file_path = 'data/devices.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                devices = json.load(file)
        else:
            return "Device not found"

        for device in devices:
            if device['device_id'] == device_id:
                self.name = device['name']
                self.device_type = device['device_type']
                self.room = [Room(**room) for room in device['room']]
                if 'status' in device:
                    self.status = device['status']
                if 'settings' in device:
                    self.settings = device['settings']
                if 'data' in device:
                    self.data = device['data']
                return

        return "Device not found in JSON file."

    # Assign (devices can work in multiple rooms)
    def add_room(self, room):
        self.room.append(room)
        self.save_device()

    def delete_room(self, room):
        for existing_room in self.room:
            if existing_room.room_id == room:
                self.room.remove(room)
                break
        self.save_device()
    
    # Read
    def get_details(self):
        return {
            'device_id': self.device_id,
            'name': self.name,
            'device_type': self.device_type,
            'room': [device_room.get_details() for device_room in self.room],
            'status': self.status,
            'settings': self.settings,
            'data': self.data
        }
    
    # Update
    def update_device(self, name = None, device_type = None, room = None, status = None, settings = None, data = None):
        if name is not None:
            if not isValidNameDevice(name):
                raise ValueError("Invalid device name")
            self.name = name
        if device_type is not None:
            if not isValidDeviceType(device_type):
                raise ValueError("Invalid device type")
            self.device_type = device_type
        if room is not None:
            self.room = room
        if status is not None:
            self.status = status
        if settings is not None:
            self.settings = settings
        if data is not None:
            self.data = data
        self.save_device()

    # Delete
    def delete_device(self):
        file_path = 'data/devices.json'

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as file:
            devices = json.load(file)

        devices = [device for device in devices if device['device_id'] != self.device_id]

        with open(file_path, 'w') as file:
            json.dump(devices, file, indent=4)

    # Search for devices?

    

