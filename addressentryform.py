import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

form_fields =['First Name', 'Last Name', 'Address Line 1', 'Address Line 2', 'City',
             'State/Province', 'Postal Code', 'Country']

entries = []


for i, form_field in enumerate(form_fields):
    label = tk.Label(window, text=f'{form_field}:')
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(window, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5,)
    entries.append(entry)


button_frame = tk.Frame(window)
button_frame.grid(row=len(form_fields), column=0, columnspan=2, padx=10, pady=10, sticky="e")

clear_button = tk.Button(button_frame, text= "Clear")
clear_button.pack(side='right', padx=5)


submit_button = tk.Button(button_frame, text= "Submit")
submit_button.pack(side='right')

window.mainloop()
