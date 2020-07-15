from tkinter import *
import backend

window = Tk()
window.title('OSIM Parts Court')

#--------------------------------------------function
def add_command():
    backend.add(entry_model_Value.get(),entry_name_Value.get(),entry_number_Value.get(),entry_qty_Value.get())
    listbox.delete(0,END)
    listbox.insert(END,(entry_model_Value.get(),entry_name_Value.get(),entry_qty_Value.get()))

#---------------------------------------------listbox
listbox = Listbox(window,height=30,width=30)
listbox.grid(row=0,column=0,rowspan=10)

sb = Scrollbar(window)
sb.grid(row=0,column=1,rowspan=6)

#---------------------------------------------label X4
label_model = Label(window,text='Model')
label_model.grid(row=0,column=1)

label_model = Label(window,text='Part Name')
label_model.grid(row=1,column=1)

label_model = Label(window,text='Part Number')
label_model.grid(row=2,column=1)

label_model = Label(window,text='QTY')
label_model.grid(row=3,column=1)

#---------------------------------------------entry X4
entry_model_Value = StringVar()
entry_model = Entry(window,textvariable=entry_model_Value)
entry_model.grid(row=0,column=2)

entry_name_Value = StringVar()
entry_name = Entry(window,textvariable=entry_name_Value)
entry_name.grid(row=1,column=2)

entry_number_Value = StringVar()
entry_number = Entry(window,textvariable=entry_number_Value)
entry_number.grid(row=2,column=2)

entry_qty_Value = StringVar()
entry_qty = Entry(window,textvariable=entry_qty_Value)
entry_qty.grid(row=3,column=2)

#---------------------------------------------button X7

#plus_button = Button(window,text='+1')
#plus_button.grid(row=4,column=2,rowspan=2)

minus_button = Button(window,text='-1',width=3)
minus_button.grid(row=4,column=2)

view_button = Button(window,text='View',width=20)
view_button.grid(row=5,column=1)

search_button = Button(window,text='Search',width=20)
search_button.grid(row=5,column=2)

update_button = Button(window,text='Update',width=20)
update_button.grid(row=6,column=1)

add_button = Button(window,text='Add',width=20,command=add_command)
add_button.grid(row=6,column=2)

close_button = Button(window,text='Close',width=20,command=window.destroy)
close_button.grid(row=7,column=2)



window.mainloop()