from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from myapp.database.database import Base
import datetime
from sqlalchemy.orm import relationship

class Card(Base):
    __tablename__ = "cards"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    anonymous = Column(Boolean, default=False)
    
    #(e.g., "Written under the cherry blossoms in Kyoto").
    location = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    theme_id = Column(String, ForeignKey("card_themes.id"))
    emotion_id = Column(String, ForeignKey("emotions.id"))
    
    emotions = relationship("Emotions", back_populates="cards")
    comments = relationship("Comment", back_populates="card")
    likes = relationship("Like", back_populates="card")

    #Partner with artists to create visual interpretations of popular haikus.
    art_colab = Column(String, index=True)

    theme = relationship("CardTheme", back_populates="cards")
    owner = relationship("User", back_populates="cards")

#A class to store the best card of the week
class BestWeek(Base):
    __tablename__ = "best_week"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    card_id = Column(String, ForeignKey("cards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    card = relationship("Card", back_populates="best_week")
    owner = relationship("User", back_populates="best_week")

#A class to store the best user of the week
class BestUser(Base):
    __tablename__ = "best_user"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="best_user")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(String, primary_key=True, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    card_id = Column(String, ForeignKey("cards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    card = relationship("Card", back_populates="comments")
    owner = relationship("User", back_populates="comments")

class Like(Base):
    __tablename__ = "likes"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    card_id = Column(String, ForeignKey("cards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    card = relationship("Card", back_populates="likes")
    owner = relationship("User", back_populates="likes")

class Emotions(Base):
    __tablename__ = "emotions"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    cards = relationship("Card", back_populates="emotion")

#A card theme class 
class CardTheme(Base):
    __tablename__ = "card_themes"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    #Styles
    background_color = Column(String, index=True)
    text_color = Column(String, index=True)
    font = Column(String, index=True)
    font_size = Column(Integer, index=True)
    border_color = Column(String, index=True)

    image = Column(String, index=True)
    cards = relationship("Card", back_populates="theme")

class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(String, primary_key=True, index=True)

    card_id = Column(String, ForeignKey("cards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    card = relationship("Card", back_populates="favorites")
    owner = relationship("User", back_populates="favorites")

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    comments = relationship("Comment", back_populates="owner")
    likes = relationship("Like", back_populates="owner")

    cards = relationship("Card", back_populates="owner")
