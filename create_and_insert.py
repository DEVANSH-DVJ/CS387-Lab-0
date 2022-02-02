import psycopg2 as pg

conn = pg.connect(database='Lab0', user='postgres',
                  password='secret', host='localhost', port='5432')
cur = conn.cursor()

with open('PS/DDL.sql', 'r') as file:
    cur.execute(file.read())
with open('PS/sampleData.sql', 'r') as file:
    cur.execute(file.read())

conn.commit()

cur.close()
if (conn):
    conn.close()
