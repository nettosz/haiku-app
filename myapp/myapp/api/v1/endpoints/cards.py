from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database.database import get_db
from myapp.schemas.schemas import CardCreate, CardList, Card, CardUpdate
from myapp.controllers.cards import create_card, read_card, read_cards, update_card, delete_card

router = APIRouter()

@router.post("/create_card")
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    id = create_card(db=db, card=card).id
    
    #return url location
    return {"location": f"/api/v1/get_card/{id}"}

@router.get("/read_card/{card_id}", response_model=Card)
def read_card(card_id: int, db: Session = Depends(get_db)):
    card = read_card(db=db, card_id=card_id)
    
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    #Card.from_orm(card)
    return Card(**card.dict())

@router.get("/read_cards", response_model=CardList)
def read_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = read_cards(db=db, skip=skip, limit=limit)
    
    return CardList(items=cards)

@router.put("/update_card/{card_id}", response_model=Card)
def update_card(card_id: int, card: CardUpdate, db: Session = Depends(get_db)):
    card = update_card(db=db, card_id=card_id, card=card)
    
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    return Card(**card.dict())

@router.delete("/delete_card/{card_id}", response_model=Card)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    card = delete_card(db=db, card_id=card_id)
    
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    
    return Card(**card.dict())

