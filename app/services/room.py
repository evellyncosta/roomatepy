from cachetools import cached, TTLCache


class RoomService:
    cache = TTLCache(maxsize=100, ttl=180)

    def cache_key(*args, **kwargs):
        return 'all_available_rooms'

    def __init__(self, room_repository):
        self.room_repository = room_repository

    def get_all_rooms(self):
        return self.room_repository.find_all()

    @cached(cache, key=cache_key)
    def get_all_available(self):
        return self.room_repository.find_all_available_rooms()

    def book_room(self, id):
        room_saved = self.room_repository.find_by_id(id)
        if room_saved:
            room_saved.available = False
            self.room_repository.save(room_saved)
            self.cache.clear()
            return room_saved
        return None
