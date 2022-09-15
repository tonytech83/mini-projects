#   GUI application - Converter from BGN to EUR

#   Import library
import tkinter as tk

#   Create graphic app with rectangular frame (Frame)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #   create widgets
        self.label = tk.Label(text="Value Converter")
        self.numberEntry = tk.Entry()
        self.converterButton = tk.Button(text="Converter", command=self.convert)
        self.output = tk.Label()
        #   place widgets
        self.label.pack(side="left")
        self.numberEntry.pack(side="left")
        self.converterButton.pack(side="left")
        self.output.pack(side="left")

    def convert(self):
        entry = self.numberEntry.get()

        try:
            value = float(entry)
            result = round(value * 1.95583, 2)
            self.output.config(text=str(value) + " BGN = " + str(result) + " EUR", bg="green", fg="white")
        except ValueError:
            self.output.config(text="That's not a number!", bg="red", fg="black")
#   Create the application
app = Application()
app.master.title("BGN to EUR Converter")

#   Start the program
app.mainloop()
