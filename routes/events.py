from typing import List
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event

event_router = APIRouter(
    tags=["Events"]
)

events = []


@event_router.get("/")
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id_}", response_model=Event)
async def retrieve_event(id_: int) -> Event:
    for event in events:
        if event.id == id_:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully."
    }


@event_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(id: int) -> None:
    for event in events:
        if event.id == id:
            events.remove(event)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully."
    }
