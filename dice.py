import tkinter as tk
import random


def roll():
    label['text'] = str(random.randint(1, 6))


window = tk.Tk()
window.rowconfigure([0, 1], weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=150)

button = tk.Button(window, text='Roll', command=roll)
button.grid(row=0, column=0, sticky='nsew')


# I am putting the text here on label but it can be left blank

label = tk.Label(text="0")
label.grid(row=1, column=0)







window.mainloop()