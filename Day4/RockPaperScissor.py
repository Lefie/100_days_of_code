import random

user=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.")
a_list=["Rock","Paper","Scissors"]
computer=random.randint(0,2)

if user!='0' and user!='1' and user!='2':
    print("Invalid")

if user=='0':
    if computer==0:
        print("Computer chose",a_list[computer])
        print("Tie")
    elif computer==1:
        print("Computer chose",a_list[computer])
        print('You lost')
    else:
        print("Computer chose",a_list[computer])
        print("You won")


if user=='1':
    if computer==0:
        print("Computer chose",a_list[computer])
        print("You won")
    elif computer==1:
        print("Computer chose",a_list[computer])
        print('Tie')
    else:
        print("Computer chose",a_list[computer])
        print("You lost")

if user=='2':
    if computer==0:
        print("Computer chose",a_list[computer])
        print("You lost")
    elif computer==1:
        print("Computer chose",a_list[computer])
        print('You won')
    else:
        print("Computer chose",a_list[computer])
        print("Tie")


