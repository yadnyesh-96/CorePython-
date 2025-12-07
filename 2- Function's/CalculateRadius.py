#Write a function that calculates the area of a circle.(Use radius as input)

def cal_radius(rad):
    return 3.14*rad*rad

print("--- Calculate the Area of Circle ---")

r=int(input("Enter the radius of circle :"))

res=cal_radius(r)

print("Area of Circle is :",res)