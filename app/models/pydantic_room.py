from pydantic import BaseModel
from typing import Optional
import uuid


class RoomBase(BaseModel):
    id: Optional[uuid.UUID]
    number: int
    available: bool

    class Config:
        orm_mode = True
