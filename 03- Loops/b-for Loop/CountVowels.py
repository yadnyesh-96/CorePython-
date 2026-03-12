'''
6. Count how many vowels are in a string
'''

text=input("Enter the text :")

Vowels='aeiouAEIOU'

count=0
for i in text:
    if i in Vowels:
       count+=1 
       
print(count)