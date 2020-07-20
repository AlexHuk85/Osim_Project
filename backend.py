import sqlite3
import pandas as pd
import numpy as np

data = 'stock.xlsx'
sheets = ['808','818','833','845','855','848','838','856','858','860','868','875','888','890','873']
my_list = []

def get_data():
    for sheet in sheets:

        df = pd.read_excel(data,sheet_name=sheet)
        value = 3
        skip = 'OS-808 Parts'

        for item in range(1000):
            try:
                if df.iloc[value,2] is np.nan:
                    pass
                else:
                    if skip in df.iloc[value,2]:
                        my_list.append((df.iloc[value,2][13:],df.iloc[value,0],df.iloc[value,3]))
                    else:
                        my_list.append((df.iloc[value,2],df.iloc[value,0],df.iloc[value,3]))
            except IndexError:
                pass
            value += 1
    return my_list

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

def search(model='',part_name='',part_number=''):
    conn = sqlite3.connect("partslist_DEMO.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM parts WHERE model LIKE ? AND part_name LIKE ? AND part_number like ?",('%'+model+'%','%'+part_name+'%','%'+part_number+'%'))
    row = cur.fetchall()
    conn.close()
    return row

#-------------------------------------------read old data from xlxs
def save_data():
    for item in get_data():
        if '808' in item[1]:
            add('808-uDivine',item[0],item[1],item[2])
        elif '818' in item[1]:
            add('818 uDivine App',item[0],item[1],item[2])
        elif '833' in item[1]:
            add('833 uDivine S',item[0],item[1],item[2])
        elif '845' in item[1]:
            add('845 uDiva',item[0],item[1],item[2])
        elif '855' in item[1]:
            add('855 uNano',item[0],item[1],item[2])
        elif '848' in item[1]:
            add('848 uInfinity Luxe',item[0],item[1],item[2])
        elif '838' in item[1]:
            add('838 uInfinity',item[0],item[1],item[2])
        elif '856' in item[1]:
            add('856 uDiva Classic',item[0],item[1],item[2])
        elif '858' in item[1]:
            add('858 uMagic',item[0],item[1],item[2])
        elif '860' in item[1]:
            add('860 uDeluxe',item[0],item[1],item[2])
        elif '868' in item[1]:
            add('868 uLove',item[0],item[1],item[2])
        elif '875' in item[1]:
            add('875 uDiva 2',item[0],item[1],item[2])
        elif '888' in item[1]:
            add('888 uLove 2',item[0],item[1],item[2])
        elif '890' in item[1]:
            add('890 uDivine V',item[0],item[1],item[2])
        elif '873' in item[1]:
            add('873 uRegal',item[0],item[1],item[2])

connect()
if len(search(model='808')) < 1:
    save_data()


