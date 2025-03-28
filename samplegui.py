import tkinter as tk
import tkinter.ttk as tkk

#the foundational element of TKINTER is the window
#it contains all other elements known as widgets

window = tk.Tk()

# Here are the widgets

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

entry = tk.Entry(
    fg= 'brown',
    bg= 'green',
    width=50
)

entry.pack()

name = entry.get()
name

#Getting Multiline User Input With Text Widgets

text = tk.Text()
text.pack()


#Assigning Widgets to Frames



#start the GUI event loop using the line below, otherwise the scipt will not display the button
window.mainloop()