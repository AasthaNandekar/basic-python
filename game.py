'''
1 for sanke
-1 for water
0 for gun
'''
import random
computer=random.choice(["snake", "water", "gun"])
you=input("enter your choice=")
print(f"computer choice={computer}")
print(f"your choice={you}")
if computer==you:
    print("tie")
else:
    if computer=="snake" and you=="water":
        print("you win")
    elif computer=="water" and you=="snake":
        print("you win")
    elif computer=="water" and you=="gun":
        print("you win")
    elif computer=="gun" and you=="water":
        print("you win")
    elif computer=="gun" and you=="snake":
        print("you win")
    elif computer=="snake" and you=="gun":
        print("you win")
    else:
        print("you lose")