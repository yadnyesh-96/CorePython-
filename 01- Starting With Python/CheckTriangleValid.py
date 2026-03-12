# Write a Python program to check whether a triangle is valid or not.

print("----- Check Triangle Valid or not -----")

side1=int(input("Enter the Side-1 :"))
side2=int(input("Enter the Side-2 :"))
side3=int(input("Enter the Side-3 :"))

res= "Valid" if side1+side2>side3 and side1+side3>side2 and side2+side3>side1 else "Not Valid"
print(res)