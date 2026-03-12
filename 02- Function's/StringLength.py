# Write a function that takes a string and returns its length.

def cal_StringLen(S):
    count=0
    for char in S:
        count+=1
    return count
    

text=input("Enter the text ")

length = cal_StringLen(text)
print("Length of string is:", length)
