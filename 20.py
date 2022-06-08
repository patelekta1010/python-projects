n=int(input("ENTER THE NUMBER :"))
print("ENTER 1 or 0 :")
bool_val=input("1 for True or 0 for False :")
i=1
if bool_val=="1":
    for i in range(0,n+1):
        print("*"*i)
if bool_val=="0":
    for i in range(n,0,-1):
        print("*"*i)

