from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes import user  # Import user router from routes folder

app = FastAPI()

# Ensure you're including the user router correctly
app.include_router(user.router, prefix="/api", tags=["users"])

# Create all tables in the database
Base.metadata.create_all(bind=engine)

@app.get("/api")
def read_root():
    return {"message": "Welcome to the FastAPI Backend"}
