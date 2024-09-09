import tkinter as tk
import pint 

ureg = pint.UnitRegistry()


#unit assigment is in the format: unit = n * type
#n is the quantity and type is the unit type I.E Km, or meters
#Type parses and can take both shortened and long version
distance = 24 * ureg.km
#print(distance)

time = 8 * ureg.second
#print(time)

speed = distance/time
#print(speed)

#CONVERSION is also possible

x = speed.to("meter/minute")
#print(x)


#ALTERNATIVELY
Q = ureg.Quantity

a = input("Type units: ")
b = input("Type unit of measurement: ")
c = a + " " + b
Q(c)
print(c)

new_unit = input("Type new unit: ")
print(Q(c).to(new_unit).magnitude)

