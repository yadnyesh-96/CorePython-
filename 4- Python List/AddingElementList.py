# Adding Elements into List
# We can add elements to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.
# clear(): removes all items.

l1=[10,20,30,40,50]

print("List",l1)
l1.append(60) #Adds an element at the end of the list.
print("After using append() = ",l1)
l1.extend([70,80,90,100]) #Adds multiple elements to the end of the list.
print("After using extend() = ",l1)
l1.insert(1,220)  #Adds an element at a specific position.
print("After using insert() = ",l1) 
l1.clear()
print("After using clear() = ",l1) 
