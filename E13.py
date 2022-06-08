n=int(input("ENTER THE NUMBER :"))
k=1
for i in range(0,n):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()

    """
       *
       * * *
       * * * * *
       * * * * * * *
    """