from user import User
from cheats import execute

class currentUser:
    def __init__(self, id):
        clone = User(id)
        self.id = clone.id
        self.username = clone.username
        self.password = clone.password
