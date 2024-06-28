import tkinter as tk
from login_form import LoginForm
from course_form import CourseForm

def main():
    root = tk.Tk()
    root.title("Форма входа")
    login_form = LoginForm(root, open_course_form)
    root.mainloop()

def open_course_form():
    root = tk.Tk()
    root.title("Форма для создания отчета")
    root.geometry("500x300")
    course_form = CourseForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
