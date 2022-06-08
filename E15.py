for row in range(5):
    for col in range(4):
        if(col==0) or (col!=0 and row%2==0):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

    # E alphabet pattern