a=9
b=8
c=sum((a,b))
print(c)
def function1(a,b) :
    print("hello! you are in function 1 ",a+b)
function1(9,8)
def function2(a,b):
    """average of two numbers"""
    average=(a+b)/2
    return average
v=function2(5,7)
print(v)
print(function2.__doc__)