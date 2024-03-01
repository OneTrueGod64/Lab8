import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
# Import the CelsiusToFahrenheitApp class
from CelsiusToFahrenheitApp import CelsiusToFahrenheitApp

class MainApp:
    def __init__(self, master):
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add Celsius to Fahrenheit calculator
        # Assuming the CelsiusToFahrenheitApp class exists and follows a similar interface
        celsius_to_fahrenheit_app = CelsiusToFahrenheitApp(self.__mainwindow)
        self.__main_notebook.add(celsius_to_fahrenheit_app.get_top_frame(), text="Celsius to Fahrenheit")

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()
