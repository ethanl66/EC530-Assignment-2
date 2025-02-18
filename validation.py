import re

def isValidID(user_id):
    return isinstance(user_id, int) and user_id > 0

# User --------------------------------------------------------
def isValidNameUser(name):
    return isinstance(name, str) and len(name) > 0 and len(name.split()) >= 2
def isValidUsername(username):
    return isinstance(username, str) and len(username) > 0 and len(username) <= 24 and username.isalnum()
def isValidPhone(phone):
    return isinstance(phone, str) # and re.fullmatch(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', phone) is not None
def isValidEmail(email):
    return isinstance(email, str) and re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) is not None

# House --------------------------------------------------------
def isValidNameHouse(name):
    return isinstance(name, str) and len(name) > 0 and len(name) <= 50
def isValidAddress(address):
    return isinstance(address, str) and len(address) > 0 and len(address) <= 100
def isValidGPS(gps_coordinates):
    return isinstance(gps_coordinates, str) and re.fullmatch(r'\d{1,3}\.\d{1,6}, \d{1,3}\.\d{1,6}', gps_coordinates) is not None
def isValidOwnerIDs(owner_ids):
    return (isinstance(owner_ids, int) and owner_ids > 0) or (isinstance(owner_ids, list) and all(isinstance(owner_id, int) and owner_id > 0 for owner_id in owner_ids))

# Room --------------------------------------------------------
def isValidNameRoom(name):
    return isinstance(name, str) and len(name) > 0 and len(name) <= 50
def isValidFloor(floor):
    return isinstance(floor, int) and floor >= 0 and floor <= 3000
def isValidSize(size):
    return isinstance(size, (int, float)) and size > 0
def isValidDimensions(dimensions):
    return len(dimensions) == 2 and all(isinstance(coord, (int, float)) and coord > 0 for coord in dimensions)
def isValidRoomType(room_type):
    return isinstance(room_type, str) and len(room_type) > 0 and len(room_type) <= 50


# Device --------------------------------------------------------
def isValidNameDevice(name):
    return isinstance(name, str) and len(name) > 0 and len(name) <= 50
def isValidDeviceType(device_type):
    return isinstance(device_type, str) and len(device_type) > 0 and len(device_type) <= 50
