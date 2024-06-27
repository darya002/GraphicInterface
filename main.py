import os
import json
import tkinter as tk
from login_form import LoginForm
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Форма входа")

    login_form = LoginForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
