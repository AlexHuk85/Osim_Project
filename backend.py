import sqlite3

def connect():
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, model TEXT, part_name TEXT, part_number TEXT, Qty INTEGER)")
    conn.commit()
    conn.close()

def add(model,part_name,part_number,Qty):
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO parts VALUES (NULL,?,?,?,?)",(model,part_name,part_number,Qty))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("partlist.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM parts")
    row = cur.fetchall()
    conn.close()
    return row



connect()
add('OS808-uDivine','testing','C808xx-xx-xxxx',5)
print(view())
