# t.me/ural_tg
import tkinter as tk
import webbrowser

def open_link():
    url = "https://t.me/ural_tg"
    webbrowser.open(url)

root = tk.Tk()
root.title("Сообщение")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Если надо, то пиши в тг", font=("Arial", 16), pady=10)
label.pack()


entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.insert(0, "t.me/ural_tg")
entry.pack(fill=tk.X, padx=20, pady=20)

# Кнопка для открытия ссылки
button = tk.Button(root, text="Написать", font=("Arial", 14), command=open_link)
button.pack(pady=10)

root.mainloop()
