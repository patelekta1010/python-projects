n=int(input("ENTER THE NUMBER :"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

    """pattern
    *
    * *
    * * *
    * * * *
    """