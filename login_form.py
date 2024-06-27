import tkinter as tk
from callbacks import on_login

class LoginForm:
    def __init__(self, master):
        self.master = master
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
        username = self.username_entry.get()
        password = self.password_entry.get()
        on_login(username, password)
