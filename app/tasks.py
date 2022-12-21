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

    def create_new(content, userid):
        execute( 'INSERT INTO `tasks` (task, userid) VALUES (\"%s\", \"%s\")' % (content, userid) )

    def complete_old(content, userid):
        execute( 'DELETE FROM `tasks` WHERE task = (\"%s\") AND userid = (\"%s"\)' % (content, userid))


        

    



        