from tkinter import *

def concatenate():
    inp = input.get()
    s, s1 = inp.split(maxsplit=1)
    output1.delete(0, END)
    output1.insert(0, s)
    output2.delete(0, END)
    output2.insert(0, s1)

root = Tk()
frame = Frame()

input = Entry(frame, width=10)
output1 = Entry(width=20, bg='lightgreen', justify=CENTER)
output2 = Entry(width=20, bg='lightgreen', justify=CENTER)
button = Button(frame, text='Разбить', command=concatenate)

frame.pack(padx=10, pady=10)
input.pack(side='left')
button.pack(side='left', padx=10)
output1.pack(side='left')
output2.pack(pady=10)

root.mainloop()