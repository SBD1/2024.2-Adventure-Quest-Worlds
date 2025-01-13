from dotenv import load_dotenv
import psycopg2
import os
import re

load_dotenv('../.env')


def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOSTNAME','localhost'),
            database=os.getenv('POSTGRES_DB','postgres'),
            user=os.getenv('POSTGRES_USER','postgres'),
            password=os.getenv('POSTGRES_PASSWORD','postgres'),
            port=os.getenv('DATABASE_PORT', 5432)
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def create_tables():
    try:
        conn = get_connection()
        cur = conn.cursor()

        with open(os.path.join(os.path.dirname(__file__), 'ddl.sql'), 'r') as f:
            ddl = f.read()

            tables = re.sub(r'\n', '', ddl.strip()).split(';')
            for table in tables:
                if table:
                    cur.execute(table)
            
        conn.commit()
        cur.close()
        conn.close()

        print("Tabelas criadas com sucesso")
            
    except psycopg2.Error as e:
        print(f"Erro ao inicializar as tabelas: {e}")