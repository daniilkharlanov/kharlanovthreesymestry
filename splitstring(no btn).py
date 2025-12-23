from tkinter import *


def concatenate(*a):
    s = var3.get()
    ans1, ans2 = s.split(maxsplit=1)
    var1.set(ans1)
    var2.set(ans2)

root = Tk()

frame = Frame()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

input1 = Entry(frame, width=10, textvariable=var3)
output1 = Entry(width=20, bg='lightgreen', justify=CENTER,
textvariable=var1)
output2 = Entry(width=20, bg='lightgreen', justify=CENTER, textvariable=var2)
var3.trace_add("write", concatenate)
frame.pack(padx=10, pady=10)
input1.pack(side='left')
output1.pack(side='left')
output2.pack(pady=10)

root.mainloop()