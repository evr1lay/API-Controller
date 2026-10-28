from contextlib import asynccontextmanager
from uuid import uuid4

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

class MessageSchema(BaseModel):
    id: str
    content: str

class MessageAddSchema(BaseModel):
    content: str

class MessageUpdateSchema(BaseModel):
    content: str | None = None

messages: list[MessageSchema] = []

@app.get("/messages")
def get_messages() -> list[MessageSchema]:
    return messages

@app.post("/messages", status_code=status.HTTP_201_CREATED)
def add_message(payload: MessageAddSchema) -> dict:
    new_message = MessageSchema(id=str(uuid4()), content=payload.content)
    messages.append(new_message)
    return {"success": True}

@app.patch("/messages/{message_id}")
def update_message(message_id: str, payload: MessageUpdateSchema):
    for message in messages:
        if message.id == message_id and payload.content:
            message.content = payload.content
        return

@app.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: str):
    for message in messages:
        if message.id == message_id:
            messages.remove(message)
        return

if __name__ == "__main__":
    config = uvicorn.Config("api:app", reload=True, port=8000)
    server = uvicorn.Server(config)
    server.run()
