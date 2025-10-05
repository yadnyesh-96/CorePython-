# Write a Python program to enter radius of a circle and find its diameter, area and circumference.
# Formulas:
# diameter = 2 * radius  
# circumference = 2 * 3.14 * radius  
# area = 3.14 * radius * radius

print("---- Find the Circle Diameter , Area and Circumference ---- ");

rad=int(input("Enter the radius of Circle: \n"));

diameter=2*rad;
print("The Diameter of the Circle is the: ",diameter);

circumference=2*3.14*rad;
print("The Circumeference of the Circle is: ",circumference);

area=3.14*rad*rad;
print("The Area of the Circle is: ",area);