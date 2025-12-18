import tkinter as tk
from tkinter import font

def clicked():
    try:
        height = float(txth.get())
        weight = float(txtw.get())

        if height <= 0 or weight <= 0:
            lblresult1.configure(text="Ошибка: рост и вес должны быть больше нуля!", fg="red")
            return

        imt = weight / (height / 100) ** 2
        imt = round(imt, 2)

        if imt < 18.5:
            result_text = f"Индекс массы тела: {imt} → недостаточная масса"
            lblresult1.configure(text=result_text, fg="#FF6B6B")
        elif 18.5 <= imt < 25:
            result_text = f"Индекс массы тела: {imt} → норма"
            lblresult1.configure(text=result_text, fg="#00FF00")
        elif 25 <= imt < 30:
            result_text = f"Индекс массы тела: {imt} → избыточная масса"
            lblresult1.configure(text=result_text, fg="#FFD93D")
        else:
            result_text = f"Индекс массы тела: {imt} → ожирение"
            lblresult1.configure(text=result_text, fg="#FF5E5E")


    except ValueError:
        lblresult1.configure(text="Ошибка: введите числа!", fg="red")



window = tk.Tk()
window.title("Калькулятор ИМТ")
window.geometry("500x400")
window.configure(bg="#F7F9F9")



default_font = font.Font(family="Helvetica", size=12)
title_font = font.Font(family="Helvetica", size=16, weight="bold")



lbltitle = tk.Label(
    window,
    text="Калькулятор индекса массы тела (ИМТ)",
    font=title_font,
    bg="#F7F9F9",
    fg="#2C3E50",
    pady=20
)
lbltitle.pack()


input_frame = tk.Frame(window, bg="#F7F9F9")
input_frame.pack(pady=10)


lblh = tk.Label(input_frame, text="Рост (см):", font=default_font, bg="#F7F9F9", fg="#34495E")
lblh.grid(column=0, row=0, padx=10, pady=10, sticky="e")
txth = tk.Entry(input_frame, width=15, font=default_font, bd=2, relief="solid")
txth.grid(column=1, row=0, padx=10, pady=10)



lblw = tk.Label(input_frame, text="Вес (кг):", font=default_font, bg="#F7F9F9", fg="#34495E")
lblw.grid(column=0, row=1, padx=10, pady=10, sticky="e")
txtw = tk.Entry(input_frame, width=15, font=default_font, bd=2, relief="solid")
txtw.grid(column=1, row=1, padx=10, pady=10)


btn = tk.Button(
    window,
    text="Рассчитать ИМТ",
    command=clicked,
    font=default_font,
    bg="#3498DB",
    fg="white",
    activebackground="#2980B9",
    relief="raised",
    padx=20,
    pady=5
)
btn.pack(pady=20)

result_frame = tk.Frame(window, bg="#F7F9F9")
result_frame.pack(pady=10)

lblresult = tk.Label(
    result_frame,
    text="Результат:",
    font=default_font,
    bg="#F7F9F9",
    fg="#7F8C8D"
)
lblresult.grid(column=0, row=0, padx=10, pady=5, sticky="w")


lblresult1 = tk.Label(
    result_frame,
    text="",
    font=("Helvetica", 11, "italic"),
    bg="#F7F9F9",
    fg="#2C3E50",
    wraplength=400,
    justify="left"
)
lblresult1.grid(column=0, row=1, padx=10, pady=5, sticky="w")


window.mainloop()



