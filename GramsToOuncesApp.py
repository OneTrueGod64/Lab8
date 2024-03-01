# CelsiusToFahrenheitApp.py
import tkinter as tk
import tkinter.messagebox as messagebox


class CelsiusToFahrenheitApp:
    def __init__(self, master=None):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.master, text="Celsius:")
        self.input_label.grid(row=0, column=0)

        self.input_entry = tk.Entry(self.master)
        self.input_entry.grid(row=0, column=1)

        self.calculate_button = tk.Button(self.master, text="Convert", command=self.calculate)
        self.calculate_button.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(self.master, text="Fahrenheit:")
        self.result_label.grid(row=2, column=0)

        self.result = tk.StringVar()
        self.result_entry = tk.Entry(self.master, textvariable=self.result, state='readonly')
        self.result_entry.grid(row=2, column=1)

    def calculate(self):
        try:
            celsius = float(self.input_entry.get())
            fahrenheit = celsius * 9 / 5 + 32
            self.result.set(f"{fahrenheit} F")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def get_top_frame(self):
        return self.master


if __name__ == "__main__":
    root = tk.Tk()
    app = CelsiusToFahrenheitApp(root)
    root.mainloop()

