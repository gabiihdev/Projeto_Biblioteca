import sqlite3

DB = "biblioteca.db"

def conectar():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = ON") 
        return conn, cursor
    
    except Exception as e:
        print(f"\n>> ERRO AO CONECTAR COM O BANCO: {e}")
        return None, None

def desconectar(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()