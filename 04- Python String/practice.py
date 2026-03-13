
def func(*arg):
    for i in arg:
        print(i)
        
func(1,2,3)

def func1(**kwarg):
    print(kwarg)
    
func1(name="yad",age=20)

add = lambda a,b:a+b
print(add(2,4))

s = {1,2,3,3,4}
print(s)