from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

## Card Schema
class CardBase(BaseModel):
    title: str
    content: Optional[str] = None
    
    owner_id:int

    class Config:
        orm_mode = True
    
class CardCreate(CardBase):
    pass

class CardUpdate(CardBase):
    pass

class Card(CardBase):
    id: str
    #
    created_at: datetime

    class Config:
        orm_mode = True

class CardList(BaseModel):
    items: List[Card]

    class Config:
        orm_mode = True

###
## User Schema
class UserBase(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserList(BaseModel):
    items: List[User]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
