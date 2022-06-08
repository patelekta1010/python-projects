n=18
guess=1
print("NUMBER OF GUESSES IS LIMITED TO 10")
while(guess<=10) :
    num=int(input("GUESS THE NUMBER : \n"))

    if num<18 :
        print("YOU ENTER LESSER NUMBER\n")
    elif num>18 :
        print("YOU ENTER GREATER NUMBER\n")
    else :
        print("YOU WON!!!!!!\n ")
        print(guess,"no. of guess you take is : ")
        break
    print(10-guess,"NO. OF GUESS LEFT")
    guess=guess+1
if(guess>10) :
    print("GAME OVER")