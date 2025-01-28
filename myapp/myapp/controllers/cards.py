from sqlalchemy.orm import Session
from myapp.models.models import Card
from myapp.schemas.schemas import CardCreate
from uuid import uuid4

def create_card(db: Session, card: CardCreate):
    db_card = Card(**card.dict())
    db_card.id = uuid4()
    
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def read_card(db: Session, card_id: int):
    return db.query(Card).filter(Card.id == card_id).first()

def read_cards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Card).offset(skip).limit(limit).all()

def update_card(db: Session, card_id: int, card: CardCreate):
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if db_card:
        for key, value in card.dict().items():
            setattr(db_card, key, value)
        
        db.commit()
        db.refresh(db_card)

    return db_card

def delete_card(db: Session, card_id: int):
    db_card = db.query(Card).filter(Card.id == card_id).first()
    db.delete(db_card)
    db.commit()
    return db_card
