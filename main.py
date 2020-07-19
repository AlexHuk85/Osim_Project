from tkinter import *
import backend

window = Tk()
window.title('OSIM Parts Court')

#--------------------------------------------function
def add_command():
    backend.add(entry_model_Value.get(),entry_name_Value.get(),entry_number_Value.get(),entry_qty_Value.get())
    listbox.delete(0,END)
    listbox.insert(END,(entry_model_Value.get(),entry_name_Value.get(),entry_qty_Value.get()))

def view_command():
    listbox.delete(0,END)
    rows = backend.view()
    for row in rows:
        listbox.insert(END,row)

def search_command():
    rows = backend.search(entry_model_Value.get(),entry_name_Value.get(),entry_number_Value.get())
    listbox.delete(0,END)  
    for row in rows:
        listbox.insert(END,row)

def minus_command():
    num = entry_qty_Value.get()
    entry_qty.delete(0,END)
    entry_qty.insert(END,int(num)-1)

    
def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        entry_model.delete(0,END)
        entry_model.insert(END,selected_tuple[1])
        entry_name.delete(0,END)
        entry_name.insert(END,selected_tuple[2])
        entry_number.delete(0,END)
        entry_number.insert(END,selected_tuple[3])
        entry_qty.delete(0,END)
        entry_qty.insert(END,selected_tuple[4])
    except IndexError:
        pass

def update_command():
    backend.update(selected_tuple[0],entry_model_Value.get(),entry_name_Value.get(),entry_number_Value.get(),entry_qty_Value.get())
    view_command()

def clear():
    entry_model.delete(0,END)   
    entry_name.delete(0,END)       
    entry_number.delete(0,END)     
    entry_qty.delete(0,END)
#---------------------------------------------listbox
listbox = Listbox(window,height=30,width=70)
listbox.grid(row=0,column=0,rowspan=10)

sb = Scrollbar(window)
sb.grid(row=0,column=1)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',get_selected_row)
#---------------------------------------------label X4
label_model = Label(window,text='Model')
label_model.grid(row=0,column=2)

label_name = Label(window,text='Part Name')
label_name.grid(row=1,column=2)

label_number = Label(window,text='Part Number')
label_number.grid(row=2,column=2)

label_qty = Label(window,text='QTY')
label_qty.grid(row=3,column=2)

#---------------------------------------------entry X4
entry_model_Value = StringVar()
entry_model = Entry(window,textvariable=entry_model_Value)
entry_model.grid(row=0,column=3)

entry_name_Value = StringVar()
entry_name = Entry(window,textvariable=entry_name_Value)
entry_name.grid(row=1,column=3)

entry_number_Value = StringVar()
entry_number = Entry(window,textvariable=entry_number_Value)
entry_number.grid(row=2,column=3)

entry_qty_Value = StringVar()
entry_qty = Entry(window,textvariable=entry_qty_Value)
entry_qty.grid(row=3,column=3)

#---------------------------------------------button X7

#plus_button = Button(window,text='+1')
#plus_button.grid(row=4,column=2,rowspan=2)

minus_button = Button(window,text='-1',width=3,command=minus_command)
minus_button.grid(row=4,column=3)

view_button = Button(window,text='View',width=20,command=view_command)
view_button.grid(row=5,column=2)

search_button = Button(window,text='Search',width=20,command=search_command)
search_button.grid(row=5,column=3)

update_button = Button(window,text='Update',width=20,command=update_command)
update_button.grid(row=6,column=2)

add_button = Button(window,text='Add',width=20,command=add_command)
add_button.grid(row=6,column=3)

close_button = Button(window,text='Close',width=20,command=window.destroy)
close_button.grid(row=7,column=3)

clear_button = Button(window,text='Clear',width=20,command=clear)
clear_button.grid(row=7,column=2)

window.mainloop()