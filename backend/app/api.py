from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db, Base, engine
from .models.event import Event as EventModel
from .models.schemas import EventCreate, EventRead, EventUpdate

# Create tables
Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "ok"}

@router.get("/events", response_model=list[EventRead])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(EventModel).offset(skip).limit(limit).all()

@router.get("/events/{event_id}", response_model=EventRead)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/events", response_model=EventRead)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = EventModel(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.put("/events/{event_id}", response_model=EventRead)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.dict(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"detail": "Event deleted"}
