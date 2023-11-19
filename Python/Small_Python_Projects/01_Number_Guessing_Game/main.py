import tkinter as tk
from tkinter import *
import random

# Creating the GUI window
win = tk.Tk()
win.geometry("700x700")
win.title("Number Guessing Game")
num = random.randint(1, 20)
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

hint.set("Guess a number between 1 to 20")
score.set(5)
final_score.set(score.get())


def fun():
    x = guess.get()
    final_score.set(score.get())
    if score.get() > 0:
        score.set(score.get() - 1)
        final_score.set(score.get())

        if num == x:
            hint.set("Congratulation YOU WON!!!")

        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")

        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")

    else:
        hint.set("Game Over You Lost")


# Creating the Labels, Entry Boxes and Button
(Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE)
 .place(relx=0.5, rely=0.3, anchor=CENTER))
(Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange')
 .place(relx=0.5, rely=0.7, anchor=CENTER))
(Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE)
 .place(relx=0.61, rely=0.85, anchor=CENTER))
(Label(win, text='I challenge you to guess the number ', font=("Courier", 25))
 .place(relx=0.5, rely=0.09, anchor=CENTER))
(Label(win, text='Score out of 5', font=("Courier", 25))
 .place(relx=0.3, rely=0.85, anchor=CENTER))
(Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue')
 .place(relx=0.5, rely=0.5, anchor=CENTER))

win.mainloop()
