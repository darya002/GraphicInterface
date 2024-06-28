import json
import os
from tkinter import messagebox

def validate_session():
    # Проверяем валидность сессии (пример)
    if os.path.exists("session.json"):
        with open("session.json", "r") as file:
            try:
                session_data = json.load(file)
                cached_username = session_data.get("username", "")
                cached_password = session_data.get("password", "")
                # Ваша логика проверки сессии здесь
                if cached_username == "user" and cached_password == "password":
                    return True
                else:
                    return False
            except json.JSONDecodeError:
                return False
    return False

def on_login(username, password, login_form):
    # Пример простой проверки логина и пароля
    if username == "user" and password == "password":
        # Сохраняем учетные данные в файл session.json
        save_session(username, password)
        messagebox.showinfo("Успешный вход", "Вы успешно вошли в систему!")
        login_form.login_successful()
    else:
        messagebox.showerror("Ошибка входа", "Неверный логин или пароль.")
        login_form.unlock()

def save_session(username, password):
    # Сохраняем учетные данные в файл session.json
    session_data = {
        "username": username,
        "password": password
    }
    with open("session.json", "w") as file:
        json.dump(session_data, file)
