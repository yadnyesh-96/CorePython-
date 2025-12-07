# Write a function that returns the reverse of a string.

def rev_String(text):
    rev=" "
    for i in text:
        rev=i+rev
    return rev

text=input("Enter the String:")
print("Reversed String : ",rev_String(text))