from fastapi import FastAPI
from myapp.api.v1.endpoints.cards import router as cards_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My FastAPI Project", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cards_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}