import pyttsx3
import tkinter as tk


def test_to_speech(text, lang='english'):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #   create widgets
        self.label = tk.Label(text="Еnter your text here:")
        self.textEntry = tk.Entry()
        self.executeButton = tk.Button(text="Execute", command=self.execution)
        #   place widgets
        self.label.pack(side="left")
        self.textEntry.pack(side="left")
        self.executeButton.pack(side="left")

    def execution(self):
        entry = self.textEntry.get()
        test_to_speech(entry)


app = App()
app.master.title("Text to Speech")

# start the program
app.mainloop()
