from tkinter import ttk
import tkinter as tk
from unit_settings import *
import pint

def is_valid(direction):
    try: 
        x = float(direction.get()) 
        return True
    except ValueError:
        print("Invalid")
        return False

def update(_):
    from_selection.config(values=unit_types[set_type.get()])
    from_selection.current(0)
    to_selection.config(values=unit_types[set_type.get()])
    to_selection.current(1)
    convert(_)

def convert(_):
    if is_valid(from_entry):
        from_unit = from_selection.get().lower()
        to_unit = to_selection.get().lower()
        amount = from_entry.get()

        a = f"{amount} {from_unit}"
        converted = Q(a).to(to_unit).magnitude
        default2.set(converted)

def reverse_conversion(_):
    if is_valid(to_entry): 
        from_unit = from_selection.get().lower()
        to_unit = to_selection.get().lower()
        amount = to_entry.get()

        a = f"{amount} {to_unit}"
        converted = Q(a).to(from_unit).magnitude
        default.set(converted)
    
# Initialize
ureg = pint.UnitRegistry()
Q = ureg.Quantity
window = tk.Tk()
window.geometry(window_size)
window.title("Unit Converter")
window.resizable(False,False)
window.config(background=bg_color)

# variables
default = tk.IntVar(value=1)
default2 = tk.IntVar(value=0)

# Set rows & columns
window.rowconfigure(list(range(3)),weight=1)
window.columnconfigure(list(range(2)),weight=1)

# Main unit selection
set_type = ttk.Combobox(window, values=main_selection, font=main_font, justify="center")
set_type.grid(row=0, columnspan=2)
set_type.current(0)
set_type.bind("<<ComboboxSelected>>", update)

# Row 1 widgets
from_label = ttk.Label(window,text="From: ", font=main_font, background="gray")
from_label.grid(row=1,column=0, padx=10,pady=10,sticky="NW")

to_label = ttk.Label(window, text="To:", font=main_font, background="gray")
to_label.grid(row=1, column=1, padx=10, pady=10, sticky="NW")

# Row 2 widgets
from_entry = ttk.Entry(window, font=main_font, textvariable=default, justify="right")
from_entry.grid(row=1, column=0)
from_entry.bind("<Any-KeyRelease>", convert)

to_entry = ttk.Entry(window, font=main_font, justify="right", textvariable=default2)
to_entry.grid(row=1, column=1)
to_entry.bind("<Any-KeyRelease>", reverse_conversion)

# Row 3 widgets
from_selection = ttk.Combobox(window, font=main_font,values=unit_types[set_type.get()], justify="center")
from_selection.grid(row=2,column=0, sticky="N")
from_selection.current(0)
from_selection.bind("<<ComboboxSelected>>", convert)


to_selection = ttk.Combobox(window, font=main_font, values=unit_types[set_type.get()], justify="center")
to_selection.grid(row=2,column=1, sticky="N")
to_selection.current(1)
to_selection.bind("<<ComboboxSelected>>", convert)
convert(1)

if __name__ == "__main__": 
    window.mainloop()
