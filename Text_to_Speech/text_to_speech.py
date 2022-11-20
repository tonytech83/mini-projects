import pyttsx3
from tkinter import *

root = Tk()


def execution():
    entry = textEntry.get()
    test_to_speech(entry)


def test_to_speech(text, lang='english'):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()


label = Label(root, text="Еnter your text here:")
label.pack()
textEntry = Entry(root, width=50)
textEntry.pack()
executeButton = Button(root, text="Execute", command=execution)
executeButton.pack()

# start the program
root.mainloop()
