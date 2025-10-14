# Write a Python program to calculate area of an equilateral triangle.
# Formula:
# area = (√3 / 4) * (side * side)

import math
print("----- To calculate the Area of Equilateral Triangle -----")

side1=int(input("Enter the Side of Equilateral Triangle (in cm): "));

area=(math.sqrt(3) / 4)*(side1**2)

print(f"Area of Equlateral Triangle is: {area:.2f} cm^2")

