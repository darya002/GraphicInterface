from tkinter import messagebox

def on_login(username, password):
    # Здесь можно добавить проверку логина и пароля
    messagebox.showinfo("Информация", f"Логин: {username}\nПароль: {password}")
