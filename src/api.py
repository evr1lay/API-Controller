from contextlib import asynccontextmanager
from typing import Annotated
from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI, status
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DATABASE_URL = "sqlite:///messages.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))

class MessageORM(Base):
    __tablename__ = "messages"

    content: Mapped[str]
    author: Mapped[str]

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

class MessageSchema(BaseModel):
    id: str
    content: str

class MessageAddSchema(BaseModel):
    content: str
    author: str

class MessageUpdateSchema(BaseModel):
    content: str | None = None
    author:  str | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def orm_to_model(message_orm: MessageORM) -> MessageSchema:
    return MessageSchema(id=message_orm.id, content=message_orm.content)

@app.get("/messages")
def get_messages(db: Annotated[Session, Depends(get_db)]) -> list[MessageSchema]:
    messages_from_db = db.scalars(select(MessageORM)).all()
    return [orm_to_model(msg) for msg in messages_from_db]

@app.post("/messages", status_code=status.HTTP_201_CREATED)
def add_message(payload: MessageAddSchema, db: Annotated[Session, Depends(get_db)]) -> dict:
    ...

@app.patch("/messages/{message_id}")
def update_message(message_id: str, payload: MessageUpdateSchema, db: Annotated[Session, Depends(get_db)]):
    ...

@app.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: str, db: Annotated[Session, Depends(get_db)]):
    ...

if __name__ == "__main__":
    config = uvicorn.Config("api:app", reload=True, port=8000)
    server = uvicorn.Server(config)
    server.run()
