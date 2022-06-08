import random

n = 1
you_win = 0
computer_win = 0
print("you can play this game for 5 times\n")
print("----------GOOD LUCK!!!----------\n")
a = "stone"
b = "paper"
c = "scissor"
while n <= 5:
    you = input("ENTER YOUR CHOICE :")
    print("you=", you)
    lst = ["stone", "paper", "scissor"]
    choice = random.choice(lst)
    print("computer =", choice)
    if you == a and choice == "paper":
        print("you lost !!")
        computer_win += 1
        print("computer points= ", computer_win)
        print("your points= ", you_win)
    elif you == b and choice == "scissor":
        print("you lost")
        computer_win += 1
        print("computer points= ", computer_win)
        print("your points= ", you_win)
    elif you == a and choice == "scissor":
        print("you lost")
        computer_win += 1
        print("computer points= ", computer_win)
        print("your points= ", you_win)
    elif you == c and choice == "stone":
        print("you lost")
        computer_win += 1
        print("computer points= ", computer_win)
        print("your points= ", you_win)
    elif you == choice:
        print("GAME IS TIE ")
    else:
        print("you win !!\n")
        you_win += 1
        print("computer points= ", computer_win)
        print("your points= ", you_win)
    print("NO. OF life left", 5 - n)
    n = n + 1
if computer_win < you_win:
    print("you win over all game")
elif computer_win == you_win:
    print("nobody win .. the game is tie")
else:
    print("you lost the over all game ")
if n > 5:
    print("computer points= ", computer_win)
    print("your points= ", you_win)
    print("------------- GAME OVER----------------")
