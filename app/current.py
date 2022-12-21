from user import User
from cheats import execute

class currentUser:
    def __init__(self, id):
        clone = User(id)
        self.id = clone.id
        self.username = clone.username
        self.password = clone.password

    def get_tasks(self):
        data = execute('SELECT * FROM `stories` WHERE `stories`.usrID=%d' % self.id).fetchall()

        if len(data) == 0:
            return None

        tasks = list()
        for s in data:
            print(s)

        return true
