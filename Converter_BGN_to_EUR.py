# GUI application - Converter from BGN to EUR

# import library - tkinter
import tkinter as tk
from forex_python.converter import CurrencyRates

# ake current rate
c = CurrencyRates()
current_rate = c.get_rate('USD', 'EUR', )
print(current_rate)


# create graphic app with rectangular frame (Frame)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #   create widgets
        self.label = tk.Label(text="Еnter the amount")
        self.numberEntry = tk.Entry()
        self.converterButton = tk.Button(text="Convert", command=self.convert)
        self.output = tk.Label()
        #   place widgets
        self.label.pack(side="left")
        self.numberEntry.pack(side="left")
        self.converterButton.pack(side="left")
        self.output.pack(side="left")

    def convert(self, current_rate):
        entry = self.numberEntry.get()

        try:
            value = float(entry)

            result = round(value * current_rate, 2)
            self.output.config(text=str(value) + " BGN = " + str(result) + " EUR", bg="green", fg="white")
        except ValueError:
            self.output.config(text="That's not a number!", bg="red", fg="black")


# create the application
app = Application()
app.master.title("BGN to EUR Converter")

# start the program
app.mainloop()
