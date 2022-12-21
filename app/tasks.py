# THIS WILL HANDLE UPDATING THE DB AFTER USER EXISTS WINDOW

from cheats import execute
from user import User
#from story_db import StoryDB

class Task:

    def __init__(self, id):

        execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id           INTEGER PRIMARY KEY,
                    task         TEXT,
                    userid       INTEGER
                )
                """
        )

        

    



        