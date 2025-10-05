# Write a Python program to calculate the Compound Interest.
# Formula:
# CI = P * ((1 + R/100)**T - 1)

print("----- Calculate the Compound Interest -----")

p=int(input("Enter the Principal Amount(Rs.): "))
r=int(input("Enter the Rate of Interest(%): "))
t=int(input("Enter the Time Period(Yrs): "))

CI=p*((1+r/100)**t-1)

print("------------------------------")
print("Principal Amount:",p,"Rs.")
print(f"Compound Interest: {CI:.2f} Rs.")
print(f"The Total Amount: {CI+p:.2f} Rs.")