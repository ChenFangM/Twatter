from user import User
from cheats import execute

class currentUser:
    def __init__(self, id):
        clone = User(id)
        self.id = clone.id
        self.username = clone.username
        self.password = clone.password

    def get_tasks(self):
        data = execute('SELECT * FROM `tasks` WHERE `tasks`.userid=%d' % self.id).fetchall()

        if len(data) == 0:
            return ["fire", "power"]

        tasks = list()
        for s in data:
            print(s)

        return data
