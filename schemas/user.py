from typing import Optional, Union
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str = None
    phone_number: int
    address: str = None
    city : str

class SearchUser(BaseModel):
    first_name: str = None
    last_name: str = None
    phone_number: int = None
    address: str = None
    city : str = None


