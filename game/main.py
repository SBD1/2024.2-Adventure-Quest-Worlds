import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432
)

cur = conn.cursor()

# this is just an example to test the connection it will be removed later
cur.execute("""
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
""")

conn.commit()

cur.close()
conn.close()
