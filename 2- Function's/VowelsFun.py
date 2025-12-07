#Write a function that counts vowels in a string

def count_vowels(text):
    count=0
    for char in text:
        if char in "aeiouAEIOU":
            count+=1
    return count

text=input("Enter the text :")

res=count_vowels(text)
print(res)