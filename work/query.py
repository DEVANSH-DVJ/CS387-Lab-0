import sys
import sqlite3 as sql

with open(sys.argv[1], 'r') as file:
    query = file.read()

try:
    DB_NAME = "univ.db"

    conn = sql.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(query)

    res = cur.fetchall()
    for row in res:
        print(','.join(str(x) for x in row))

    cur.close()

# Error handling
except Exception as error:
    print(error)

# Close the connection
finally:
    if (conn):
        conn.close()
