from config.database import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("DROP SCHEMA public CASCADE;")
cur.execute("CREATE SCHEMA public;")
conn.commit()