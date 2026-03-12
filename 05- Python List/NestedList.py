# Nested Lists
# A nested list is a list within another list, 
# which is useful for representing matrices or tables.
# We can access nested elements by chaining indexes.

M=[[1,2,3],[4,5,6],[7,8,9]]

for i in M:
    print("[",end="")
    for j in i:
        print(j,end=" ")
    print("]")