import time
i=0
while(True) :
    inp=int(input("ENTER THE NUMBER\n"))
    if inp>100 :
        print("NUMBER IS GREATER THAN 100\n")
        break

    else:
        print(("TRY AGAIN"))
        continue

print(time.asctime())