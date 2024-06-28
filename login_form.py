import tkinter as tk
from callbacks import on_login


class LoginForm:
    def __init__(self, master, on_success):
        self.master = master
        self.on_success = on_success
        self.create_widgets()

    def create_widgets(self):
        # Создаем и размещаем метки и поля ввода
        self.username_label = tk.Label(self.master, text="Логин")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.master, text="Пароль")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        # Создаем и размещаем кнопку
        self.login_button = tk.Button(self.master, text="Войти", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        # Заблокировать элементы
        self.username_entry.configure(state="disabled")
        self.password_entry.configure(state="disabled")
        self.login_button.configure(state="disabled")

        username = self.username_entry.get()
        password = self.password_entry.get()

        # Вызываем функцию on_login для обработки входа
        on_login(username, password, self)

    def unlock(self):
        # Разблокировать элементы
        self.username_entry.configure(state="normal")
        self.password_entry.configure(state="normal")
        self.login_button.configure(state="normal")

    def close(self):
        self.master.destroy()

    def login_successful(self):
        self.close()
        self.on_success()
