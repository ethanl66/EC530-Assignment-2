from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    houses: List['House'] = []  # forward reference

class House(BaseModel):
    id: Optional[int] = None
    address: str
    owner_id: int
    residents_ids: List[int] = []