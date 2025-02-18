import json
import os
from validation import *

class User:
    # Create
    def __init__(self, user_id, name, username, phone, email):
        self.user_id = user_id
        if not isValidID(self.user_id):
            raise ValueError("Invalid user ID")
        self.name = name
        if not isValidNameUser(self.name):
            raise ValueError("Invalid name")
        self.username = username
        if not isValidUsername(self.username):
            raise ValueError("Invalid username")
        self.phone = phone
        if not isValidPhone(self.phone):
            raise ValueError("Invalid phone number")
        self.email = email
        if not isValidEmail(self.email):
            raise ValueError("Invalid email address")
        self.houses = []

        # Save user to .json file
    def save_user(self):
        file_path = 'data/users.json'
        user_data = self.get_details()

        # Ensure the "data" directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Initialize an empty list if the file doesn't exist or is empty/invalid
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            users = []
        else:
            try:
                with open(file_path, 'r') as file:
                    users = json.load(file)
            except json.JSONDecodeError:
                # If the file contains invalid JSON, initialize an empty list
                users = []

        # Check if the user already exists and update their data
        user_found = False
        for user in users:
            if user['user_id'] == self.user_id:
                user.update(user_data)
                user_found = True
                break

        # If the user doesn't exist, append their data
        if not user_found:
            users.append(user_data)

        # Write the updated list of users back to the file
        with open(file_path, 'w') as file:
            json.dump(users, file, indent=4)

    # Load user from .json file
    def load_user(self, user_id):
        file_path = 'data/users.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                users = json.load(file)
        else:
            return "User not found"

        for user in users:
            if user['user_id'] == user_id:
                self.name = user['name']
                self.username = user['username']
                self.phone = user['phone']
                self.email = user['email']
                self.houses = user['houses']
                break
        else:
            return "User not found"

    # Assign (Users can have houses)
    def add_house(self, house):
        self.houses.append(house)
        self.save_user()

    def delete_house(self, house_id):
        for house in self.houses:
            if house.house_id == house_id:
                self.houses.remove(house)
        self.save_user()

    # Read
    def get_details(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'phone': self.phone,
            'email': self.email,
            'houses': [house.get_details() for house in self.houses]
        }
    
    # Update
    def update_user(self, name = None, username = None, phone = None, email = None):
        if name is not None:
            if not isValidNameUser(name):
                raise ValueError("Invalid name")
            self.name = name
        if username is not None:
            if not isValidUsername(username):
                raise ValueError("Invalid username")
            self.username = username
        if phone is not None:
            if not isValidPhone(phone):
                raise ValueError("Invalid phone number")
            self.phone = phone
        if email is not None:
            if not isValidEmail(email):
                raise ValueError("Invalid email address")
            self.email = email
        self.save_user()

    # Delete
    def delete_user(self):
        file_path = 'data/users.json'

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as file:
            users = json.load(file)

        users = [user for user in users if user['user_id'] != self.user_id]

        with open(file_path, 'w') as file:
            json.dump(users, file, indent=4)

    # search for user?