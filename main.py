import tkinter as tk
from tkinter import messagebox
import json
import os


def on_login():
    login = login_entry.get()
    password = password_entry.get()
    if not login or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль.")
        return
    login_button.config(state=tk.DISABLED)
    login_entry.config(state=tk.DISABLED)
    password_entry.config(state=tk.DISABLED)

    # Здесь должен быть код для проверки логина и пароля
    # Например, проверка с использованием session.json

    # Эмулируем проверку:
    if login == "admin" and password == "password":
        messagebox.showinfo("Успех", "Вы вошли в систему.")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")
        login_button.config(state=tk.NORMAL)
        login_entry.config(state=tk.NORMAL)
        password_entry.config(state=tk.NORMAL)


def check_session():
    if os.path.exists("session.json"):
        try:
            with open("session.json", "r") as file:
                session = json.load(file)
                login_entry.insert(0, session.get("login", ""))
                # Здесь можно добавить проверку валидности сессии
        except json.JSONDecodeError:
            messagebox.showerror("Ошибка", "Файл session.json некорректен.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("Авторизация")

tk.Label(root, text="Логин").grid(row=0, column=0)
login_entry = tk.Entry(root)
login_entry.grid(row=0, column=1)

tk.Label(root, text="Пароль").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Войти", command=on_login)
login_button.grid(row=2, columnspan=2)

check_session()

root.mainloop()
