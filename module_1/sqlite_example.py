import sqlite3
import queries as q


# DB connect function
# 1 connection = sqlite3.connect('rpg_db.sqlite3')
# in function form
def connect_to_db(db_mane='rpg_db.sqlite3'):
    return sqlite3.connect(db_mane)


# The steps bellow in a function
# 2 cursor = connection.cursor()
# 3 results = cursor.execute(q.SELECT_ALL).fetchall()
def execute_q(conn, query):
    # make the "cursor"
    curs = conn.cursor()
    # execute the query
    curs.execute(query)
    # pull the results and return
    return curs.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.SELECT_ALL))
