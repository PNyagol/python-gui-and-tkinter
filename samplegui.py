import tkinter as tk

window = tk.Tk()

#Button

button = tk.Button(
    window,
    text= "Click Me",
    width= 25,
    height=5,
    bg="blue",
    fg="white" )

button.pack()

#Label

label = tk.Label(
    window,
    text= "I am Prof. Peter Nyagol",
    width=40,
    height=10,
    background="black",
    foreground="red")

label.pack()


#Getting user inputs with entry Widgets




#start the GUI event loop using the line below, otherwise the scipt will not display the button
window.mainloop()