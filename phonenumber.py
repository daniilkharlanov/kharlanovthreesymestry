from tkinter import *
from tkinter import ttk

def number(txt):
    label.configure(text=txt)


root = Tk()
root.geometry('800x400')
frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

var = IntVar()
var.set(0)
lbl_info = Label(root, text='Здравствуйте, данная телефонная книга позволит вам увидеть интересующий вас номер телефона').pack()
Radiobutton(frame, text='Даниил',indicatoron=False, command=lambda: number('+7-999-999-99-99'),
variable=var, value=0, width=10, height=2).pack(anchor=W)
Radiobutton(frame, text='Степан', indicatoron=False, command=lambda: number('+7-991-531-12-21'),
variable=var, value=1, width=10, height=2).pack(anchor=W)
Radiobutton(frame, text='Владислав', indicatoron=False, command=lambda: number('+7-123-456-78-90'),
variable=var, value=2, width=10, height=2).pack(anchor=W)
lbl = Label(root, width=20, height=2, text='Номер телефона:').pack(anchor="center")
label = Label(width=20, height=2, text='number phone', bg='white')
label.pack()
frame.pack(anchor=NW, fill=Y, padx=5, pady=5)

root.mainloop()
