class Room:
    def __init__(self, name):
        self.name = name
        self.occupants = set()

    def join(self, user):
        self.occupants.add(user)

    def leave(self, user):
        self.occupants.discard(user)

    def get_occupants(self):
        return self.occupants.copy()


class RoomManager:
    def __init__(self):
        self.rooms = {}

    def get_room(self, name):
        return self.rooms.get(name)

    def create_room(self, name):
        if name not in self.rooms:
            self.rooms[name] = Room(name)
        return self.rooms[name]

    def remove_room(self, name):
        if name in self.rooms:
            self.rooms.pop(name)