from contextlib import asynccontextmanager
from uuid import uuid4

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("📗 API is running")
    yield
    print("📕 API is stopped")

app = FastAPI(lifespan=lifespan)

class MessageSchema(BaseModel):
    id: str
    content: str

class MessageAddSchema(BaseModel):
    content: str

messages: list[MessageSchema] = []

@app.get("/messages")
def get_messages() -> list[MessageSchema]:
    return messages

@app.post("/messages", status_code=status.HTTP_201_CREATED)
def add_message(payload: MessageAddSchema) -> dict:
    new_message = MessageSchema(id=str(uuid4()), content=payload.content)
    messages.append(new_message)
    return {"success": True}
