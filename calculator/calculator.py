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
        self.variable_f = tk.StringVar(master=self, value='')
        self.variable_e = tk.StringVar(master=self, value='0')

        self.nlist = ['']
        self.joined_number = None

        self.x = None
        self.y = None
        self.s = None

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
        if (number == '0' and len(self.nlist) == 1) or (number == '.' and number in self.nlist): 
            pass
        elif len(self.nlist) == 1 and number == '.':
            self.nlist.append('0')
            self.nlist.append('.')
            self.joined_number = ''.join(self.nlist)
            self.variable_e.set(value=self.joined_number)
        else: 
            self.nlist.append(number)
            self.joined_number = ''.join(self.nlist)
            self.variable_e.set(value=self.joined_number)

    def clear(self, partial=False): 
        if not partial:
            self.variable_e.set('0')
            self.variable_f.set('')
            self.y = None
            self.s = None
        self.nlist.clear()
        self.nlist.append('')
        self.joined_number = None

    def make_negative(self): 
        input_is_not_empty = len(self.nlist) != 1
        is_negative = self.nlist[0] == '-'

        if input_is_not_empty and not is_negative:
            self.nlist[0] = '-'
            self.joined_number = ''.join(self.nlist)
            self.variable_e.set(self.joined_number)
        elif input_is_not_empty and is_negative:
            self.nlist[0] = ''
            self.joined_number = ''.join(self.nlist)
            self.variable_e.set(self.joined_number)
        else: pass

    def make_percentage(self):
        entry_is_not_empty = len(self.nlist) > 1
        formula_bar_is_empty = self.variable_f.get() == ''
        
        if entry_is_not_empty and not formula_bar_is_empty:
            self.joined_number = float(self.joined_number) / 100
            self.joined_number = str(self.joined_number)
            self.variable_e.set(self.joined_number)
    
    def operation(self, symbol):
        formula_bar_is_empty = self.variable_f.get() == ''

        if self.joined_number and not self.y and not self.s:
            self.x = self.joined_number
            self.s = symbol
            self.variable_f.set(f"{self.joined_number} {symbol}")
            self.clear(partial=True)

        if self.joined_number and not formula_bar_is_empty:
            self.y = self.joined_number
            self.calculate(x=self.x, y=self.y, symbol=self.s, new_symbol=symbol)

    def calculate(self, x, y, symbol, new_symbol):
        if ('.' in x) or ('.' in y):
            x = float(x)
            y = float(y)
        else:
            x = int(x)
            y = int(y)

        try:
            match symbol:
                case '+': self.x = x + y
                case '-': self.x = x - y
                case '/': self.x = x / y
                case 'x': self.x = x * y
                case _: pass
            self.variable_e.set(f'{self.x}')
            self.variable_f.set(f'{self.x} {new_symbol}')
            self.x = str(self.x)
            self.s = new_symbol
            self.clear(partial=True)

        except ZeroDivisionError:
            self.clear()
            self.variable_e.set('Cannot Divide by zero')

        if new_symbol == '=':
            self.clear()
            self.variable_e.set(str(self.x))
            self.variable_f.set(f'{x} {symbol} {y} {new_symbol} {self.x}')

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
        equal = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['=']['character'], row=MATH_OPERATORS['=']['row'], col=MATH_OPERATORS['=']['col'])
        divide = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['/']['character'], row=MATH_OPERATORS['/']['row'], col=MATH_OPERATORS['/']['col'])
        subtract = Operator(parent=self,func=self.operation, symbol=MATH_OPERATORS['-']['character'], row=MATH_OPERATORS['-']['row'], col=MATH_OPERATORS['-']['col'])
        multiply = Operator(parent=self, func=self.operation, symbol=MATH_OPERATORS['*']['character'], row=MATH_OPERATORS['*']['row'], col=MATH_OPERATORS['*']['col'])
    
    def start_actions(self):
        clear = Action(parent=self, func=self.clear, symbol=ACTION_OPERATORS['clear']['text'], row=ACTION_OPERATORS['clear']['row'], col=ACTION_OPERATORS['clear']['col'])
        negative = Action(parent=self, func=self.make_negative, symbol=ACTION_OPERATORS['negative']['text'], row=ACTION_OPERATORS['negative']['row'], col=ACTION_OPERATORS['negative']['col'])
        percent = Action(parent=self, func=self.make_percentage, symbol=ACTION_OPERATORS['percent']['text'], row=ACTION_OPERATORS['percent']['row'], col=ACTION_OPERATORS['percent']['col'])
            
class Number(tk.Button):
    def __init__(self, parent, number, row, col, span, func): 
        super().__init__(master = parent,
                         text = number,
                         font = SUB_FONT,
                         bd=1,
                         background = NUM_BUTTON_COLOR,
                         foreground = 'BLACK',
                         #activebackground="#2b2b2b",
                         padx = 10,
                         pady = 10,
                         command = lambda: func(number))
        self.grid(row=row,
                  column=col,
                  columnspan=span,
                  sticky="NEWS")

class Operator(tk.Button):
    def __init__(self, parent, symbol, row, col, func): 
        super().__init__(master = parent,
                         text = symbol,
                         font = SUB_FONT,
                         bd=1,
                         background = OPERATOR_BUTTON_COLOR,
                         foreground= 'WHITE',
                         #activebackground="White"
                         padx = 10,
                         pady = 10,
                         command = lambda: func(symbol))
        self.grid(row=row,
                  column=col,
                  sticky='NESW')

class Action(tk.Button):
    def __init__(self, parent, symbol, row, col, func): 
        super().__init__(master = parent,
                         text = symbol,
                         font = SUB_FONT,
                         bd=1,
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

#TODO Allow for keyboard inputs