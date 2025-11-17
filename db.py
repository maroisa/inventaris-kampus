import sqlite3


def init_db():
    try:
        conn = sqlite3.connect("inventaris.db")
        conn.row_factory = sqlite3.Row
        print("Connected to SQLite successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite: {e}")
