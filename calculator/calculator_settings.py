# Fonts
MAIN_FONT = "Helvetica 50"
SUB_FONT = "Helvetica 25"

# Window Settings
APP_DIMENSIONS = "400x600"
IS_RESIZABLE = (False, False)

# Column x Row Length
ROW_LENGTH = [0,1,2,3,4,5,6]
COLUMN_LENGTH = [0,1,2,3]

# Widget Placement information
NUM_POSITIONS = {
    '.': {"col": 2, "row": 6, "span": 1},
    0: {"col": 0, "row": 6, "span": 2},
    1: {"col": 0, "row": 5, "span": 1},
    2: {"col": 1, "row": 5, "span": 1},
    3: {"col": 2, "row": 5, "span": 1},
    4: {"col": 0, "row": 4, "span": 1},
    5: {"col": 1, "row": 4, "span": 1},
    6: {"col": 2, "row": 4, "span": 1},
    7: {"col": 0, "row": 3, "span": 1},
    8: {"col": 1, "row": 3, "span": 1},
    9: {"col": 2, "row": 3, "span": 1},
}

MATH_OPERATORS = {
    '/': {"col": 3, "row": 2, "character": "/", "operator": "/"},
    '*': {"col": 3, "row": 3, "character": "x", "operator": "*"},
    '-': {"col": 3, "row": 4, "character": "-", "operator": "-"},
    '+': {"col": 3, "row": 5, "character": "+", "operator": "+"},
    '=': {"col": 3, "row": 6, "character": "=", "operator": "="},
}

ACTION_OPERATORS = {
    'clear': {"col": 0, "row": 2, "text": "AC"},
    'negative': {"col": 1, "row": 2, "text": "+/-"},
    'percent': {"col": 2, "row": 2, "text": "%"},
}

# Hex Colors
BG_COLOR = "#000000"
NUM_BUTTON_COLOR = "#222222"
ACTION_BUTTON_COLOR = "#A9A9A9"
OPERATOR_BUTTON_COLOR = "#e08c24"