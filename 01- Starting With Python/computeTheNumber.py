# Write a Python program and compute the sum of an integer’s digits.
# Example: Input: 123 → Output: 6


print("----- Compute the Number  ----")

no=int(input("Enter the Three Digit Number: "))

hunders=no//100  # 123//100 ->1
tens=(no//10)%10 # (123//10)--> 12%10 --> 2
ones=no%10      #  123 % 3 --> 3

print("Compute Number:",hunders+tens+ones)  # 1+2+3 --> 6
