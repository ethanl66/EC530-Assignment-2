import json
import os
from validation import *

class House:
    def __init__(self, house_id, name, address, gps_coordinates, owner_ids, occupant_ids):
        self.house_id = house_id
        if not isValidID(house_id):
            raise ValueError("Invalid house ID")
        self.name = name
        if not isValidNameHouse(name):
            raise ValueError("Invalid house name")
        self.address = address
        if not isValidAddress(address):
            raise ValueError("Invalid address")
        self.gps_coordinates = gps_coordinates
        if not isValidGPS(gps_coordinates):
            raise ValueError("GPS coordinates must be in the format 'xx.xx, xx.xx'")
        self.owner_ids = owner_ids if owner_ids is not None else []      # can be a list of User objects
        self.occupant_ids = occupant_ids if occupant_ids is not None else []     # can be a list of User objects
        if not isValidOwnerIDs(owner_ids):
            raise ValueError("Invalid owner IDs")
        if not isValidOwnerIDs(occupant_ids):
            raise ValueError("Invalid occupant IDs")
        self.rooms = []

    # Save house to .json file
    def save_house(self):
        file_path = 'data/houses.json'
        house_data = self.get_details()

        # Ensure the "data" directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Initialize an empty list if the file doesn't exist or is empty/invalid
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            houses = []
        else:
            try:
                with open(file_path, 'r') as file:
                    houses = json.load(file)
            except json.JSONDecodeError:
                # If the file contains invalid JSON, initialize an empty list
                houses = []

        # Check if the house already exists and update their data
        house_found = False
        for house in houses:
            if house['house_id'] == self.house_id:
                house.update(house_data)
                house_found = True
                break

        # If the house doesn't exist, append their data
        if not house_found:
            houses.append(house_data)

        # Write the updated list of houses back to the file
        with open(file_path, 'w') as file:
            json.dump(houses, file, indent=4)

    # Load house from .json file
    def load_house(self, house_id):
        file_path = 'data/houses.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                houses = json.load(file)
        else:
            return "House not found"

        for house in houses:
            if house['house_id'] == house_id:
                self.name = house['name']
                self.address = house['address']
                self.gps_coordinates = house['gps_coordinates']
                self.owners = house['owners']
                self.occupants = house['occupants']
                self.rooms = house['rooms']
                break
        else:
            return "House not found"
            

    # Assign (houses can have multiple rooms, owners, and occupants)
    def add_room(self, room):
        self.rooms.append(room)
        self.save_house()

    def delete_room(self, room_id):
        if not isValidID(room_id):
            raise ValueError("Invalid room ID")
        for room in self.rooms:
            if room.room_id == room_id:
                self.rooms.remove(room)
        self.save_house()

    def add_owner(self, owner_id):
        if not isValidID(owner_id):
            raise ValueError("Invalid owner ID")
        if owner_id not in self.owner_ids:
            self.owner_ids.append(owner_id)
        self.save_house()
    
    def delete_owner(self, owner_id):
        if not isValidID(owner_id):
            raise ValueError("Invalid owner ID")
        for existing_owner_id in self.owner_ids:
            if existing_owner_id == owner_id:
                self.owner_ids.remove(owner_id)
        self.save_house()

    def add_occupant(self, occupant_id):
        if not isValidID(occupant_id):
            raise ValueError("Invalid occupant ID")
        if occupant_id not in self.occupant_ids:
            self.occupant_ids.append(occupant_id)
        self.save_house()

    def delete_occupant(self, occupant_id):
        if not isValidID(occupant_id):
            raise ValueError("Invalid occupant ID")
        for existing_occupant_id in self.occupant_ids:
            if existing_occupant_id == occupant_id:
                self.occupants.remove(existing_occupant_id)
        self.save_house()

    # Read
    def get_details(self):
        return {
            'house_id': self.house_id,
            'name': self.name,
            'address': self.address,
            'gps_coordinates': self.gps_coordinates,
            'owners': self.owner_ids,
            'occupants': self.occupant_ids,
            'rooms': [room.get_details() for room in self.rooms]
        }
    
    # Update
    def update_house(self, name = None, address = None, gps_coordinates = None, owner_ids = None, occupant_ids = None):
        if name is not None:
            if not isValidNameHouse(name):
                raise ValueError("Invalid house name")
            self.name = name
        if address is not None:
            if not isValidAddress(address):
                raise ValueError("Invalid address") 
            self.address = address
        if gps_coordinates is not None:
            if not isValidGPS(gps_coordinates):
                raise ValueError("GPS coordinates must be in the format 'xx.xx, xx.xx'")
            self.gps_coordinates = gps_coordinates
        if owner_ids is not None:
            if not isValidOwnerIDs(owner_ids):
                raise ValueError("Invalid owner IDs")
            self.owner_ids = owner_ids
        if occupant_ids is not None:
            if not isValidOwnerIDs(occupant_ids):
                raise ValueError("Invalid occupant IDs")
            self.occupant_ids = occupant_ids
        self.save_house()

    # Delete
    def delete_house(self):
        file_path = 'data/houses.json'

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as file:
            houses = json.load(file)

        houses = [house for house in houses if house['house_id'] != self.house_id]

        with open(file_path, 'w') as file:
            json.dump(houses, file, indent=4)

    # search for house?