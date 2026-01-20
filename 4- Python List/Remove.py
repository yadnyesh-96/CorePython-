# remove(): Removes the first occurrence of an element.

L=[20,20,25,30,35,40,45,50]
print("before Remove the element in List =",L)
L.remove(20)
print("After Remove the element in List =",L)

value=L.pop(3)
print(f"pop element is {value} and List is ={L}")

del L[0] # delete the specific index valu
print("After deleting element",L)
