from fastapi import APIRouter, HTTPException
from typing import List
from app.services.room import RoomService
from app.repositories.room import RoomRepository
from app.database.connection import Connection
from app.models.pydantic_room import RoomBase

router = APIRouter()


connection = Connection('mysql+pymysql://roommate:roommate@db/roommate')
room_repository = RoomRepository(connection)
room_service = RoomService(room_repository)
@router.get("/rooms", response_model=List[RoomBase])
def get_all_rooms():
    return room_service.get_all_rooms()

@router.get("/rooms/available", response_model=List[RoomBase])
def get_all_available():
    return room_service.get_all_available()

@router.get("/rooms/book/{id}", response_model=RoomBase)
def book_room(id: str):
    room = room_service.book_room(id)
    if room:
        return room
    else:
        raise HTTPException(status_code=404, detail="Room not found")
