#Given a score out of 100, print:
#Excellent (≥90)
#Good (≥75)
#Average (≥50)
#Poor (<50)
#Using nested ternary operators.

print("--- Student Grade System ---");

mark=int(input("Enter the Marks:"));

res= "Excellent" if mark>=90 else "Good" if mark>=75 else "Average" if mark>=50 else "Poor"

print("Grade :",res);