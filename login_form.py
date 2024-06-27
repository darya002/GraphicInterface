import json
import os
import tkinter as tk
from callbacks import on_login, validate_session
from tkinter import messagebox


class LoginForm:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.check_session()

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

    def check_session(self):
        # Проверяем сессию при запуске формы
        session_valid = validate_session()
        if not session_valid:
            # Если сессия невалидна, загружаем данные из session.json (если есть)
            self.load_session_data()

    def load_session_data(self):
        if os.path.exists("session.json"):
            with open("session.json", "r") as file:
                session_data = json.load(file)
                cached_username = session_data.get("username", "")
                cached_password = session_data.get("password", "")
                self.username_entry.insert(0, cached_username)
                self.password_entry.insert(0, cached_password)

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
