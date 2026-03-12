

str = "Python";
# print(str[::-1])

def revrseString(s):
    reversed_s=""
    for char in s:
        reversed_s=char+reversed_s
    return reversed_s


print(revrseString(str));