from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from myapp.database.database import Base
import datetime
from sqlalchemy.orm import relationship

class Card(Base):
    __tablename__ = "cards"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="cards")

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    cards = relationship("Card", back_populates="owner")
