from tkinter import *

def paint(txt):
    label.configure(text=txt)


root = Tk()
var = IntVar()
var.set(0)
Radiobutton(text='Даниил',indicatoron=False, command=lambda: paint('+7-999-999-99-99'),
variable=var, value=0).pack()
Radiobutton(text='Степан', indicatoron=False, command=lambda: paint('+7-991-531-12-21'),
variable=var, value=1).pack()
Radiobutton(text='Владислав', indicatoron=False, command=lambda: paint('+7-123-456-78-90'),
variable=var, value=2).pack()
label = Label(width=20, height=5, text='number phone')
label.pack()

root.mainloop()