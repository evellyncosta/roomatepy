from app.database.connection import Connection
from app.models.room import Room

class RoomRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def find_all(self):
        return self.connection.get_session().query(Room).all()

    def find_all_available_rooms(self):
        return self.connection.get_session().query(Room).filter_by(available=True).all()

    def find_by_id(self, id):
        return self.connection.get_session().query(Room).get(id)

    def save(self, room):
        session = self.connection.get_session()
        if room.id is None:
            session.add(room)
        else:
            room = session.merge(room)
        session.commit()
        return room
