import sqlite3

DB_FILE = "coffeebuds.db"

def execute(command):
    with sqlite3.connect(DB_FILE) as db:
            c = db.cursor()
            result = c.execute(command)
            db.commit()
    return result


def setup():
    execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id           INTEGER PRIMARY KEY,
                    username     TEXT,
                    password     TEXT
                )
                """
            )

    execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id           INTEGER PRIMARY KEY,
                    task         TEXT,
                    userid       INTEGER
                )
                """
    )

    execute(
                """
                INSERT INTO users (username, password)
                SELECT 'hello', 'bye'
                WHERE NOT EXISTS
                    (SELECT username, password
                    FROM users
                    WHERE username = 'hello' AND password = 'bye')
                """
    )

    execute(
                """
                INSERT INTO tasks (task, userid)
                SELECT 'study for math test', '1'
                WHERE NOT EXISTS
                    (SELECT task, userid
                    FROM tasks
                    WHERE task = 'study for math test' AND userid = '1')
                """
    )

    # execute(
    #            """
    #            INSERT INTO
    #            """
    # )
