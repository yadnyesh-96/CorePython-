# Write a Python program to enter two angles of a triangle and find the third angle.
# Third Angle=180°−(60°+80°)=40°

print("-----  To Find the third Angle From two angles  ------")

an1=int(input("Enter the first angle: \n"))
an2=int(input("Enter the Second angle: \n"))

an3=180-(an1+an2)

print("First angle is: ",an1,"°","\n Second angle is: ",an2,"°")
print("Third angle of the Triangle is: ",an3,"°")

print("-------------------------")