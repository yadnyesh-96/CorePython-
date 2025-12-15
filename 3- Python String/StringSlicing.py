# String slicing in python 
# String slicing means extracting a part (substring) from a string.
# Syntax === > string[start : end : step]

str1="Python"

print(str1[:]) # to prints full string 
print(str1[1:4]) # characters from 1 to 4 end index (exluded)
print(str1[:2])  # upto index 1
print(str1[2:])  # from 2 index to last prints
print(str1[::-1]) # reversing string 
print(str1[-5:-2]) # negative index slicing  
print(str1[::3])  # prints every third number 
print(str1[:6:2]) # every 2 number

