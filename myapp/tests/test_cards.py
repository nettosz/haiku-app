from fastapi.testclient import TestClient
from myapp.main import app  # Adjust the import based on your project structure

client = TestClient(app)

def test_create_card():
    response = client.post("/api/v1/create_card",
                           json={"title": "Test Card",
                                "description": "Test description",
                                "owner_id": 1})
    
    assert response.status_code == 200
    assert "location" in response.json()

def test_read_card():
    # First, create a card to read
    create_response = client.post("/api/v1/create_card",
                                  json={"title": "Test Card",
                                        "description": "Test description",
                                        "owner_id": 1})
    
    card_id = create_response.json()["location"].split("/")[-1]
    
    # Now, read the card
    response = client.get(f"/api/v1/read_card/{card_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Card"

def test_read_cards():
    response = client.get("/api/v1/read_cards")
    assert response.status_code == 200
    assert isinstance(response.json()["items"], list)

def test_update_card():
    # First, create a card to update
    create_response = client.post("/api/v1/create_card",
                                  json={"title": "Test Card",
                                        "description": "Test description",
                                        "owner_id": 1})
    
    card_id = create_response.json()["location"].split("/")[-1]
    
    # Now, update the card
    response = client.put(f"/api/v1/update_card/{card_id}",
                          json={"title": "Updated Card",
                                "description": "Updated description",
                                "owner_id": 1})
    
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Card"

def test_delete_card():
    # First, create a card to delete
    create_response = client.post("/api/v1/create_card",
                                  json={"title": "Test Card",
                                        "description": "Test description",
                                        "owner_id": 1})
    
    card_id = create_response.json()["location"].split("/")[-1]
    
    # Now, delete the card
    response = client.delete(f"/api/v1/delete_card/{card_id}")
    assert response.status_code == 200
    assert response.json() == {"id": card_id}