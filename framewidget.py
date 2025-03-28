import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()


frame_a.pack()
frame_b.pack()

label_a = tk.Label(master=frame_a, text='I am in FRAME A')
label_a.pack()


label_b = tk.Label(master=frame_b, text='I am in FRAME B')
label_b.pack()

window.mainloop()

