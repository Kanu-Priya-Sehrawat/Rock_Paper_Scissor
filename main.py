# This is project of Game : Rock, Paper and Scissor

import random

def game(comp, you):
    if comp == you:
        print(" The game tie ")
        return

    if comp == "r":
        if you == "p":
            print(" You Win ")
        else:
            print(" You lose ")

    elif comp == 'p':
        if you == 's':
            print(" You Win ")
        else:
            print(" You lose ")

    else:
        if you == 'r':
            print(" You Win ")
        else:
            print(" You lose ")
    
print("Computer turn : Choose Rock(r), Paper(p) and Scisoor(s) ")
rand_number = random.randint(1,3)

if rand_number==1:
    comp = "r"
elif rand_number==2:
    comp = "p"
else:
    comp = "s"

you = (input("Your turn : Choose Rock(r), Paper(p) and Scissor(s) : "))

game(comp, you)

print(f" Computer chose {comp} and you chose {you} ")