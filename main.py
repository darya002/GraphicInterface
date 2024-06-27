import os
import tkinter as tk
from login_form import LoginForm

def main():
    root = tk.Tk()
    root.title("Форма входа")

    if not os.path.exists("session.json"):
        login_form = LoginForm(root)

    root.mainloop()

if __name__ == "__main__":
    main()
