import tkinter as tk
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

def farenheit_to_celcius():
    farenheit = ent_temp.get()
    celcius = (5 / 9) * (float(farenheit) - 32)
    lbl_results['text'] = f'{round(celcius, 2)} \N{DEGREE CELSIUS}'

entry = tk.Frame(window)
ent_temp =tk.Entry(entry, width=10)
label = tk.Label(entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0, column=0, sticky='e')
label.grid(row=0, column=1, sticky="w")

btn_converter = tk.Button(window, text="Convert", command=farenheit_to_celcius)

lbl_results = tk.Label(window, text="\N{DEGREE CELSIUS}")

entry.grid(row=0, column=0, padx=10)
btn_converter.grid(row=0, column=1, padx=10)
lbl_results.grid(row=0, column=2, padx=10)
window.mainloop()