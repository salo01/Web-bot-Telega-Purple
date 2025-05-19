from pydantic import BaseModel

class EventBase(BaseModel):
    name: str
    description: str | None = None

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class EventRead(EventBase):
    id: int
    class Config:
        orm_mode = True
