# Import necessary modules
import os
import pygubu
import tkinter as tk
from tkinter import messagebox

# Define paths for accessing UI design
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "Fahrenheit_to_celsius.ui")


# Main application class for temp converter
class FahrenheitToCelsiusApp:
    # Initialize application
    def __init__(self, master=None):
        # Initialize pygubu builder and load UI file
        self.builder = pygubu.Builder()
        self.builder.add_from_file(PROJECT_UI)

        # Get main frame widget from UI file
        self.main_frame = self.builder.get_object('main_frame', master)
        # Connect event callbacks
        self.builder.connect_callbacks(self)

        # Configure grid layout
        self.configure_grid()

        # Get UI components
        self.fahrenheit_label = self.builder.get_object('fahrenheit_label')
        self.fahrenheit_entry = self.builder.get_object('fahrenheit_entry')
        self.convert_button = self.builder.get_object('convert_button')
        self.celsius_label = self.builder.get_object('celsius_label')
        self.celsius_result = self.builder.get_object('celsius_result')

        # Configure layout of UI components
        self.fahrenheit_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.fahrenheit_entry.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")
        self.convert_button.grid(row=1, column=1, columnspan=2, padx=2, pady=3, sticky="ew")
        self.celsius_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.celsius_result.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")

    # Configure grid weights
    def configure_grid(self):
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=3)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

    # Handle conversion logic on convert button click
    def on_convert_clicked(self):
        # Get input value from entry widget
        fahrenheit_str = self.fahrenheit_entry.get()
        try:
            # Perform conversion - Fahrenheit to Celsius
            fahrenheit = float(fahrenheit_str)
            celsius = (fahrenheit - 32) * 5 / 9
            # Display result in celsius_result entry widget
            self.celsius_result.delete(0, tk.END)
            self.celsius_result.insert(0, f'{celsius: .2f}')
        except ValueError:
            # Display an error message if input is invalid
            messagebox.showerror("Error", "Invalid input. Please enter valid number")

    # Return main frame widget
    def get_top_frame(self):
        return self.main_frame

    # Start app event loop
    def run(self):
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.mainloop()


# Main script entry point
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Temperature Converter Application")
    # Create and start application
    app = FahrenheitToCelsiusApp(root)
    app.run()
