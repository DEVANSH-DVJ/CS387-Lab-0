import psycopg2 as pg

with open('DDL.sql', 'r') as file:
    crt = file.read()
with open('sampleData.sql', 'r') as file:
    ins = file.read()

conn = pg.connect(database='univ', user='postgres',
                  password='secret', host='localhost', port='5432')
cur = conn.cursor()

for x in crt.split(';') + ins.split(';'):
    try:
        cur.execute(x)
        conn.commit()
    except Exception:
        continue

cur.close()

if (conn):
    conn.close()
