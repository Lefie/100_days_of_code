import random

#greeting 
greeting  = "Welcome to the Number Guessing Game!"
print(greeting)

#randomly select a number betweem 1 and 100
random_number = random.randint(1,100)
print(random_number)

choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

easy_attempt = 5
hard_attempt = 10
has_won = False

if choose_level == 'easy':
    while easy_attempt > 0:

        guess = int(input("Make a guess: "))
        if guess == random_number:
            has_won = True
            break
        elif guess > random_number:
            print("Too high")
            easy_attempt -= 1
            print(f"You have {easy_attempt} remaining")
        else:
            print("Too low")
            easy_attempt -= 1
            print(f"You have {easy_attempt} remaining")

    if has_won == True:
        print("You won")
    else:
        print("You lost")
elif choose_level == "hard":
    while hard_attempt > 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            has_won = True
            break
        elif guess > random_number:
            print("Too high")
            hard_attempt -= 1
            print(f"You have {hard_attempt} remaining")
        else:
            print("Too low")
            hard_attempt -= 1
            print(f"You have {hard_attempt} remaining")

    if has_won == True:
        print("You won")
    else:
        print("You lost")





    