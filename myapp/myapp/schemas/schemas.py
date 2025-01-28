from pydantic import BaseModel
from typing import List, Optional

## Card Schema
class CardBase(BaseModel):
    title: str
    content: Optional[str] = None
    
    data:str
    user_id:int

class CardCreate(CardBase):
    pass

class CardUpdate(CardBase):
    pass

class Card(CardBase):
    id: int

    class Config:
        orm_mode = True

class CardList(BaseModel):
    items: List[Card]

    class Config:
        orm_mode = True

###