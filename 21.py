l=10 #global variable
def ekta(n):
   # l=7  #local scope
    i=9
    global l
    l=l+4
    print(l,i)
    print(n,"I HAVE PRINTED")    #n first che bcoz mare n (this is me) ,aa statement karta pela print karau che
ekta("this is me")
print(l)