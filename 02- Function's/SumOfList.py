#Write a function that takes a list and returns the sum of all elements.

def elements_sum(Ls):
    sum=0
    for i in Ls:
        sum+=i
    return sum

Ls1=[1,2,3,4,5,6,7,8,9,10]

res=elements_sum(Ls1)

print(res)