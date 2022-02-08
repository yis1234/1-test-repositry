"""Area and volume of a sphere
Finds the area and volume of a sphere
Sun Woo Yi
07/02/22
"""
radius = float(input("What is the radius in cm: "))
area = 4 * 3.141592 * radius * radius
volume = 4 / 3 * 3.141592 * radius * radius * radius
print("{:.2f} square centimetres".format(area))
print("{:.2f} cubic centimetres".format(volume))
