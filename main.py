import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from FahrenheitToCelsiusApp import FahrenheitToCelsiusApp


class MainApp:
    def __init__(self, master):
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Build UI
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column=0, row=0, sticky='nsew')
        self.__main_notebook.rowconfigure(0, weight=1)
        self.__main_notebook.columnconfigure(0, weight=1)

        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__main_notebook)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add Fahrenheit to Celsius calculator
        fahrenheit_to_celsius_app = FahrenheitToCelsiusApp(self.__mainwindow)
        self.__main_notebook.add(fahrenheit_to_celsius_app.get_top_frame(), text="Fahrenheit to Celsius")

    def run(self):
        self.__main_notebook.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()
