import tkinter as tk
from tkinter import ttk
from calculator_settings import *


class App(tk.Tk):
    def __init__(self, title) -> None:

        # Main Set-Up
        super().__init__()
        self.title(title)
        self.geometry(APP_DIMENSIONS)
        self.resizable(*IS_RESIZABLE)
        self.config(bg=BG_COLOR) 

        # Variables
        self.variable_f = tk.StringVar(master=self, value="Formula")
        self.variable_e = tk.StringVar(master=self, value="0")
        self.variable_p = tk.StringVar(master=self, value="")
        self.nlist = list()

        # Window Layout 
        self.rowconfigure(ROW_LENGTH, uniform="a",weight=1)
        self.columnconfigure(COLUMN_LENGTH, uniform="a",weight=1)

        # Widgets
        self.create_entries()
        self.start_numbers()
        self.start_operators()
        self.start_actions()

        # Run
        self.mainloop()

    def set(self, number):
        if (number == "0" and len(self.nlist) == 0) or (number == "." and number in self.nlist): 
            pass
        elif len(self.nlist) == 0 and number == ".":
            self.nlist.append("0")
            self.nlist.append(".")
            self.variable_e.set(value="".join(self.nlist))
        else: 
            self.nlist.append(number)
            self.variable_e.set(value="".join(self.nlist))

    def clear(self): 
        self.variable_e.set("0")
        self.nlist.clear()
        self.variable_f.set("")
        self.variable_p.set("")  

    def make_negative(self): 
        ...

    def make_percentage(self):
        ...
    def get_result(self):
        ...
    
    def operation(self):
        ...

    def create_entries(self): 
        formula = ttk.Label(master=self,
                            textvariable=self.variable_f,
                            background=BG_COLOR,
                            foreground="White",
                            anchor="se",
                            font=SUB_FONT)
        formula.grid(row=0,
                     columnspan=4,
                     sticky="NEWS")

        entry = ttk.Label(master=self,
                          textvariable=self.variable_e,
                          background=BG_COLOR,
                          foreground="White",
                          anchor="se",
                          font=MAIN_FONT)
        entry.grid(row=1,
                   columnspan=4,
                   sticky="NEWS")
    
    def start_numbers(self):
        button_dot = Number(self, func=self.set, number=".", row=NUM_POSITIONS["."]['row'], col=NUM_POSITIONS["."]['col'],span=NUM_POSITIONS["."]['span'])
        button_0 = Number(self,func=self.set, number="0", row=NUM_POSITIONS[0]['row'], col=NUM_POSITIONS[0]['col'],span=NUM_POSITIONS[0]['span'])
        button_1 = Number(self,func=self.set, number="1", row=NUM_POSITIONS[1]['row'], col=NUM_POSITIONS[1]['col'],span=NUM_POSITIONS[1]['span'])
        button_2 = Number(self,func=self.set, number="2", row=NUM_POSITIONS[2]['row'], col=NUM_POSITIONS[2]['col'],span=NUM_POSITIONS[2]['span'])
        button_3 = Number(self,func=self.set, number="3", row=NUM_POSITIONS[3]['row'], col=NUM_POSITIONS[3]['col'],span=NUM_POSITIONS[3]['span'])
        button_4 = Number(self,func=self.set, number="4", row=NUM_POSITIONS[4]['row'], col=NUM_POSITIONS[4]['col'],span=NUM_POSITIONS[4]['span'])
        button_5 = Number(self,func=self.set, number="5", row=NUM_POSITIONS[5]['row'], col=NUM_POSITIONS[5]['col'],span=NUM_POSITIONS[5]['span'])
        button_6 = Number(self,func=self.set, number="6", row=NUM_POSITIONS[6]['row'], col=NUM_POSITIONS[6]['col'],span=NUM_POSITIONS[6]['span'])
        button_7 = Number(self,func=self.set, number="7", row=NUM_POSITIONS[7]['row'], col=NUM_POSITIONS[7]['col'],span=NUM_POSITIONS[7]['span'])
        button_8 = Number(self,func=self.set, number="8", row=NUM_POSITIONS[8]['row'], col=NUM_POSITIONS[8]['col'],span=NUM_POSITIONS[8]['span'])
        button_9 = Number(self,func=self.set, number="9", row=NUM_POSITIONS[9]['row'], col=NUM_POSITIONS[9]['col'],span=NUM_POSITIONS[9]['span'])
    
    def start_operators(self):
        add = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['+']['character'], row=MATH_OPERATORS['+']['row'], col=MATH_OPERATORS['+']['col'])
        equal = Operator(parent=self, func=self.get_result, symbol=MATH_OPERATORS['=']['character'], row=MATH_OPERATORS['=']['row'], col=MATH_OPERATORS['=']['col'])
        divide = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['/']['character'], row=MATH_OPERATORS['/']['row'], col=MATH_OPERATORS['/']['col'])
        subtract = Operator(parent=self,func=self.operation, symbol=MATH_OPERATORS['-']['character'], row=MATH_OPERATORS['-']['row'], col=MATH_OPERATORS['-']['col'])
        multiply = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['*']['character'], row=MATH_OPERATORS['*']['row'], col=MATH_OPERATORS['*']['col'])
    
    def start_actions(self):
        clear = Action(parent=self, func=self.clear, symbol=ACTION_OPERATORS['clear']['text'], row=ACTION_OPERATORS['clear']['row'], col=ACTION_OPERATORS['clear']['col'])
        negative = Action(parent=self, func=..., symbol=ACTION_OPERATORS['negative']['text'], row=ACTION_OPERATORS['negative']['row'], col=ACTION_OPERATORS['negative']['col'])
        percent = Action(parent=self, func=..., symbol=ACTION_OPERATORS['percent']['text'], row=ACTION_OPERATORS['percent']['row'], col=ACTION_OPERATORS['percent']['col'])

class Number(tk.Button):
    def __init__(self, parent, number, row, col, span, func): 
        super().__init__(master = parent,
                         text = number,
                         font = SUB_FONT,
                         background = NUM_BUTTON_COLOR,
                         foreground = 'WHITE',
                         #activebackground="#2b2b2b",
                         padx = 10,
                         pady = 10,
                         command = lambda: func(number))
        self.grid(row=row,
                  column=col,
                  columnspan=span,
                  sticky="NEWS")

    def update_display(self): 
        print("hello")

class Operator(tk.Button):
    def __init__(self, parent, symbol, row, col, func): 
        super().__init__(master = parent,
                         text = symbol,
                         font = SUB_FONT,
                         background = OPERATOR_BUTTON_COLOR,
                         foreground= 'BLACK',
                         #activebackground="White"
                         padx = 10,
                         pady = 10,
                         command = func)
        self.grid(row=row,
                  column=col,
                  sticky='NESW')

class Action(tk.Button):
    def __init__(self, parent, symbol, row, col, func): 
        super().__init__(master = parent,
                         text = symbol,
                         font = SUB_FONT,
                         background = ACTION_BUTTON_COLOR,
                         foreground= 'WHITE',
                         #activebackground="White"
                         padx = 10,
                         pady = 10,
                         command = func)
        self.grid(row=row,
                  column=col,
                  sticky='NESW')

if __name__ == '__main__':
    App('Calculator')
