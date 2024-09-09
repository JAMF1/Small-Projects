# settings.py
window_size = "500x300"
main_font = "Helvetica 14"
bg_color = "gray"

main_selection = ["Length",
             #"Temperature",
             "Area",
             "Volume",
             "Weight",
             "Time"]

unit_types = {
    "Length": ["Kilometer", "Meter", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Square Kilometer", "Square Meter", "Square Mile", "Acre", "Hectare"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Cubic Centimeter"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce", "Ton"],
    "Time": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]
}
