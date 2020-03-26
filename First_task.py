"""
Writing a basic program to calculate area of a circle
Area of a circle is pi multiplied by the square of the radius
I'll have the user supply the value of the radius
The value for pi is 3.142, but we're going to import math and access it from the library
"""


import math 
r = int (input ("Enter the radius of the circle: "))
area = math.pi * r * r
print ("Area of the circle is", area)
