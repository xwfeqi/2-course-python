import tkinter as tk
from tkinter import messagebox
from api.country_api import fetch_country_info

class CountryInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Інформація про країну")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Введіть назву країни:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.country_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.country_entry.pack(pady=5)

        self.search_button = tk.Button(root, text="Пошук", command=self.get_country_info, font=("Arial", 12))
        self.search_button.pack(pady=10)

        self.info_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 10), state="disabled", width=40, height=10)
        self.info_text.pack(pady=10)

    def get_country_info(self):
        country_name = self.country_entry.get().strip()
        if not country_name:
            messagebox.showwarning("Увага", "Будь ласка, введіть назву країни.")
            return

        data = fetch_country_info(country_name)
        if data:
            info_text = (
                f"Назва країни: {data['name']}\n"
                f"Столиця: {data['capital']}\n"
                f"Регіон: {data['region']}\n"
                f"Населення: {data['population']}\n"
                f"Площа: {data['area']} км²\n"
                f"Валюта: {data['currency']}\n"
            )

            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, info_text)
            self.info_text.config(state="disabled")
        else:
            messagebox.showerror("Помилка", "Країну не знайдено або виникла помилка при запиті.")
