import sqlite3

def connect():
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY,part_name text, part_number text, Qty integer,model text)")
    conn.commit()
    conn.close()

def add(part_name,part_number,Qty,model):
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO parts WHERE part_name=?,part_number=?,Qty=?,model=?",(part_name,part_number,Qty,model))
    conn.commit()
    conn.close()



connect()
add('testing','C808xx-xx-xxxx',5,'OS808-uDivine')
