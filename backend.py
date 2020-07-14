import sqlite3

def connect():
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, model TEXT, part_name TEXT, part_number TEXT, qty INTEGER)")
    conn.commit()
    conn.close()

def add(model,part_name,part_number,qty):
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO parts VALUES (NULL,?,?,?,?)",(model,part_name,part_number,qty))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM parts")
    row = cur.fetchall()
    conn.close()
    return row

def update(id,model,part_name,part_number,qty):
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("UPDATE parts SET model=?,part_name=?,part_number=?,qty=? WHERE id=?",(model,part_name,part_number,qty,id))
    conn.commit()
    conn.close()

def search(model='',part_name='',part_number='',qty=''):
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM parts WHERE model LIKE ? OR part_name LIKE ? OR part_number LIKE ?",('%'+model+'%','%'+part_name+'%','%'+part_number+'%'))
    row = cur.fetchall()
    conn.close()
    return row

connect()
add('OS808-uDivine','testing','C808xx-xx-xxxx',5)
add('OS868-uLove', 'Up Down Motor', 'C868XX-XX-F19',10)
#update(1,'OS808-uDivine','Kneading motor','C808xx-xx-xxxx',5)
#print(search(part_name='Kneading motor'))
print(view())
