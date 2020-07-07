import sqlite3

def connect():
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY,part_name text, part_number text, Qty integer,model text)")
    conn.commit()
    conn.close()