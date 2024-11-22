import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from src.utils import open_file_dialog, save_file_dialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.file_path = None
        self.create_menu()
        self.text_area = self.create_text_area(self.root)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
     
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Новий", command=self.new_file)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        file_menu.add_command(label="Зберегти як", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Закрити", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Скасувати", command=self.undo_action)
        edit_menu.add_separator()
        edit_menu.add_command(label="Вирізати", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Копіювати", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Вставити", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menu_bar.add_cascade(label="Правка", menu=edit_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self.about)
        menu_bar.add_cascade(label="Допомога", menu=help_menu)

        self.root.config(menu=menu_bar)

    def new_file(self):
        self.file_path = None
        self.text_area.delete(1.0, tk.END)
        self.root.title("Новий документ - Text Editor")

    def open_file(self):
        content, self.file_path = open_file_dialog()
        if content is not None:
            self.text_area.delete(1.0, tk.END) 
            self.text_area.insert(tk.END, content)
            self.root.title(f"{self.file_path} - Text Editor")

    def save_file(self):
        if self.file_path is None:
            self.save_file_as()
        else:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Збереження", "Файл успішно збережено!")

    def save_file_as(self):
        content = self.text_area.get(1.0, tk.END)
        self.file_path = save_file_dialog(content)
        if self.file_path:
            self.root.title(f"{self.file_path} - Text Editor")

    def create_text_area(self, window):
        text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True)
        text_area.pack(fill=tk.BOTH, expand=True)
        return text_area

    def undo_action(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

    def about(self):
        messagebox.showinfo("Про програму", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
