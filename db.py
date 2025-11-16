import psycopg2


def init_db():
    try:
        conn = psycopg2.connect(
            database="inventaris",
            user="rin",
            password="blank",
            host="localhost",
            port="5432",
        )
        print("Connected to PostgreSQL successfully!")
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
