from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    houses_ids: List[int] = []  

class House(BaseModel):
    id: Optional[int] = None
    address: str
    owner_id: int
    residents_ids: List[int] = []
    rooms_ids: Optional[List[int]] = []

class Room(BaseModel):
    id: Optional[int] = None
    name: str
    house_id: int
    devices_ids: Optional[List[int]] = []

class Device(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    status: dict[str, int] = {}
    settings: dict[str, ] = {}
    data: dict[str, ] = {}
    rooms_ids: List[int] = []