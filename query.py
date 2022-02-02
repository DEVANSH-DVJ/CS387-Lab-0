import sys
import psycopg2 as pg

with open(sys.argv[1], 'r') as file:
    query = file.read()

conn = pg.connect(database='Lab0', user='postgres',
                  password='secret', host='localhost', port='5432')
cur = conn.cursor()

cur.execute(query)

res = cur.fetchall()
for row in res:
    print(','.join(str(x) for x in row))

cur.close()
if (conn):
    conn.close()
