#Write a function that takes a list of numbers and returns the maximum element.

def max_element(Ls):
        max=Ls[0]
        for i in range(1,len(Ls)):
            if Ls[i]>=max:
                max=Ls[i]
        return max
    
Ls1=[10,45,15,20,5,56]

res=max_element(Ls1)
print(res)