import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class CourseForm:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Создаем и размещаем метку и поле ввода для ссылки на курс или идентификатора
        self.course_label = tk.Label(self.master, text="Ссылка на курс или идентификатор:")
        self.course_label.pack(pady=10)

        self.course_entry = tk.Entry(self.master, width=50)
        self.course_entry.pack(pady=5)

        # Создаем и размещаем метку и поле ввода для пути к выходной директории (только для чтения)
        self.output_label = tk.Label(self.master, text="Путь к выходной директории:")
        self.output_label.pack(pady=10)

        self.output_entry = tk.Entry(self.master, width=50, state="readonly")
        self.output_entry.pack(pady=5)

        # Создаем кнопку выбора директории с значком папки
        self.select_dir_button = tk.Button(self.master, text="Выбрать директорию", command=self.select_directory)
        self.select_dir_button.pack(pady=10)

        # Создаем кнопку "Создать отчет" с обработчиком события
        self.create_report_button = tk.Button(self.master, text="Создать отчет", command=self.create_report)
        self.create_report_button.pack(pady=20)

    def select_directory(self):
        # Обработчик кнопки выбора директории
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.output_entry.configure(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, selected_dir)
            self.output_entry.configure(state="readonly")

    def create_report(self):
        # Обработчик кнопки "Создать отчет"
        course_link = self.course_entry.get()
        output_dir = self.output_entry.get()

        # Допустим, здесь будет логика создания отчета
        # Например, проверка введенных данных и создание файла отчета
        if course_link and output_dir:
            messagebox.showinfo("Отчет создан", "Отчет успешно создан.")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля перед созданием отчета.")
