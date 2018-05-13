import sqlite3
from sqlite3 import Error


db_name = "../db_matcha.sqlite3"

def db_connect(sql, arguments=None):
    # create a database connection to a SQLite database
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        if arguments:
            c.execute(sql,arguments)
        else:
            c.execute(sql)
        conn.commit()
        return c.fetchall()
    except Error as e:
        return e
    finally:
        conn.close()


if __name__ == '__main__':
    res = db_connect('SELECT * FROM stocks WHERE trans = ?', ['BUY'])
    print(res)

