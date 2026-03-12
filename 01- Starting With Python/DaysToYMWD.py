 # Write a Python program to convert days into years, months, and weeks.

print(" ---- Day's --> Years --> Months --> Weeks ----")

days=int(input("Enter the Day's: "))

yrs=days/365
month=days/30
weeks=days/7
d=days/1

print("--------------------------------")
print(f"{d:.2f} DD:\n{weeks:.2f} WW:\n{month:.2f} MM:\n{yrs:.2f} YY")
print("--------------------------------")
