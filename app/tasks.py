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

    def create_new(content, user):
        execute( 'INSERT INTO `tasks` (task, userid) VALUES (\"%s\", \"%s\")' % (content, user.id) )

    def complete_old(content, user):
        content = content[1:]
        execute( 'DELETE FROM `tasks` WHERE task = (\"%s\") AND userid = (\"%s\")' % (content, user.id))


        

    



        