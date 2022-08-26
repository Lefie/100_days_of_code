print("Welcome to Treasure Island. Your mission is to find the treasure")

ask=input("Left or Right")

if ask.lower()=="right"or ask.lower()!="left":
    print("Game over")
else:
    ask=input("Swim or wait?")
    if ask.lower()=="swim" or ask.lower()!="wait":
        print("Game over")
    else:
        ask=input("Which door?")
        if ask.lower()=="red":
            print("Burned by fire")
        elif ask.lower()=="blue":
            print("Eaten by beasts")
        elif ask.lower()!="yellow":
            print("Game over")
        else:
            print("You Win")

