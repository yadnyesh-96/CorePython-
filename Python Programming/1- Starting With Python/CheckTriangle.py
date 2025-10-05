# Write a Python program to check whether a triangle is Equilateral, Isosceles, or Scalene.

print("----- triangle is Equilateral, Isosceles, or Scalene ------- ")

side1=float(input("Enter the Side-2: "))
side2=float(input("Enter the Side-2: "))
side3=float(input("Enter the Side-3: "))

if (side1+side2>side3) and (side1+side3>side2) and (side2+side2>side1):
    print("Triangle is Valid")
    
    if side1==side2==side3:
        print("Triangle is Equilateral ")
    elif side1==side2 or side1==side3 or side2==side3:
        print("Triangle is Isosceles ")
    else:
        print("Triangle is scalen")
else:
    print("Triangle is notValid")    