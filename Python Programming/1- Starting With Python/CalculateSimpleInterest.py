# Write a Python program to calculate the Simple Interest.
# Formula:
# SI = (P * R * T) / 100

print("----- Calculate the Simple Interest ------")

p=int(input("Enter the Principal Amount(Rs.): "))
r=int(input("Enter the Rate of Interest(%): "))
t=int(input("ENter the Time period(Yr): "))

SI=(p*r*t)/100
print("Pricipal Amount",p,"Rs.")
print("Interest :",SI)
print("The Total Amount: ",SI+p,"Rs.")
