n=int(input("ENTER THE NUMBER :"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


    """
        * * * * 
         * * *
          * *
           *
    """