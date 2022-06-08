# lamda function or anonymous functions
# new way to make function
def add(a,b):
    return a+b
minus = lambda x,y: x-y
print(add(9,4))
print(minus(5,9))

def a_first(a):
    return a[1]
a=[[1,4],[5,6],[0,3]]
a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)
print(a)