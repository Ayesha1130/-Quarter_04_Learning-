# Import required modules from FastAPI and Pydantic
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

# -----------------------------------------------
# Initialize the FastAPI app with metadata
# -----------------------------------------------
app = FastAPI(
    title="DACA Chatbot API",  # Title shown in Swagger docs
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",  # API description
    version="0.1.0",  # Version of the API
)

# -----------------------------------------------
# Define complex Pydantic models for validation
# -----------------------------------------------

# Metadata model includes a timestamp and session ID
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))  # Auto-generated current timestamp
    session_id: str = Field(default_factory=lambda: str(uuid4()))  # Random unique session ID

# Message model to accept input from users
class Message(BaseModel):
    user_id: str  # ID of the user sending the message
    text: str  # The actual message text
    metadata: Metadata  # Nested metadata
    tags: list[str] | None = None  # Optional tags (list of strings)

# Response model defines the structure of the chatbot's reply
class Response(BaseModel):
    user_id: str  # User ID for whom the response is generated
    reply: str  # Chatbot's response message
    metadata: Metadata  # Metadata such as timestamp and session ID

# -----------------------------------------------
# Define API endpoints
# -----------------------------------------------

# Root endpoint (GET): Just returns a welcome message
@app.get("/")
async def root():
    return {
        "message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."
    }

# User endpoint (GET): Returns user info based on path and optional query parameters
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    # If no role is provided, default to "guest"
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info

# Chat endpoint (POST): Accepts a Message, returns a Response
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    # Validate that the message text is not empty
    if not message.text.strip():
        raise HTTPException(
            status_code=400,  # Bad Request
            detail="Message text cannot be empty"
        )

    # Generate a simple reply using the input text
    reply_text = (
        f"Hello, {message.user_id}! You said: '{message.text}'. "
        "How can I assist you today?"
    )

    # Return a Response object with auto-generated metadata
    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()
    )

