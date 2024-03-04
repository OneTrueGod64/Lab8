import tkinter as tk
from tkinter import ttk, messagebox

class CelsiusToFahrenheitApp:
    def __init__(self, master=None):
        self.master = master
        self.top_frame = ttk.Frame(self.master)  # Create a frame as the top container
        self.top_frame.grid(row=0, column=0, sticky="nsew")  # Position the frame

        self.create_widgets()

    def create_widgets(self):
        # Use self.top_frame as the parent widget instead of self.master
        self.input_label = tk.Label(self.top_frame, text="Celsius:")
        self.input_label.grid(row=0, column=0)

        self.input_entry = tk.Entry(self.top_frame)
        self.input_entry.grid(row=0, column=1)

        self.calculate_button = tk.Button(self.top_frame, text="Convert", command=self.calculate)
        self.calculate_button.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(self.top_frame, text="Fahrenheit:")
        self.result_label.grid(row=2, column=0)

        self.result = tk.StringVar()
        self.result_entry = tk.Entry(self.top_frame, textvariable=self.result, state='readonly')
        self.result_entry.grid(row=2, column=1)

    def calculate(self):
        try:
            celsius = float(self.input_entry.get())
            fahrenheit = celsius * 9 / 5 + 32
            self.result.set(f"{fahrenheit} F")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def get_top_frame(self):
        # Return the top container frame to be added to the notebook
        return self.top_frame

