import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    filename = entry.get()
    if not filename:
        return
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(1.0, content)
    except Exception as e:
        text.delete(1.0, tk.END)
        text.insert(1.0, f"Ошибка: {str(e)}")
def save_file():
    filename = entry.get()
    if not filename:
        return
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            content = text.get(1.0, tk.END)
            file.write(content)
    except Exception as e:
        text.delete(1.0, tk.END)
        text.insert(1.0, f"Ошибка сохранения: {str(e)}")
root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("600x500")
label = tk.Label(root, text="Имя файла:")
label.pack(pady=5)
entry = tk.Entry(root, width=15)
entry.pack(pady=5)
text = tk.Text(root, height=20, width=70)
text.pack(pady=20, padx=10)
button_frame = tk.Frame(root)
button_frame.pack(pady=25)
open_button = tk.Button(button_frame, text="Открыть", command=open_file, width=15)
open_button.pack(side=tk.LEFT, padx=50)
save_button = tk.Button(button_frame, text="Сохранить", command=save_file, width=15)
save_button.pack(side=tk.LEFT, padx=5)
root.mainloop()