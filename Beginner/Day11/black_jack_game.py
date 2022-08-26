"""
Rules:
Goal: add up your cards to the largest number without going over 21
if it goes over 21, you lose 
J : 10
Q : 10
K : 10
A : 1 or 11

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
computer has to keep drawing cards until they go over 16
"""
from tkinter import Y

from matplotlib.pyplot import draw
import art
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]



#dealing one of the card
def deal_card(user):
    user.append(random.choice(cards))
    return user


def detect_black_jack(cards):
    ace = 11
    ten = 10
    if ace in cards and ten in cards :
        return True
    else:
        return False




def calculate_scores(user):
    if len(user) == 0:
        return 0
    score = 0
    count = 0
    while (count < len(user)):
        score += user[count]
        count += 1
    
    return score 


def ace_or_one(user):
    eleven = 11
    total = 0
    for i in range(len(user)):
        total += user[i]
    if eleven in user and total > 21:
        for i in range(len(user)):
            if user[i] == 11:
                user[i] = 1
    
    return user

def reveal_first_card(user):
    return user[0]



def computer_draw(user):
    total = calculate_scores(user) 
    chance = [0,1]
    
    if total < 17:
        while (total < 17):
            deal_card(user)
            total = calculate_scores(user)
    else:
        draw_or_not = random.choice(chance)
        if draw_or_not == 1:
            print("Computer is drawing a card")
            deal_card(user)
            total = calculate_scores(user)


    return user





"""
Test
"""



def game():
    answer = input("Do you want to play the game of blackjack? 'y' for yes and 'n' for no: ")
    while answer == 'y':
        print(art.logo)
        computer = []
        human = []
        computer_won = False
        human_won = False
        isTie = False

        #starting the game, we deal two cards to human 
        deal_card(human)
        deal_card(human)
        ace_or_one(human)
        human_score = calculate_scores(human)
        print(f"Your cards: {human},current score: {human_score}")
    
            
        # deal two cards to computer 
        deal_card(computer)
        deal_card(computer)
        ace_or_one(computer)
        computer_score = calculate_scores(computer)
        computer_first_card = reveal_first_card(computer)
        print(f"Computer's first card {computer_first_card}")

        human_has_black_jack = detect_black_jack(human)
        computer_has_black_jack = detect_black_jack(computer)
        
        if human_has_black_jack and not computer_has_black_jack:
            human_won = True
            print("You have won! Computer went over")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
            answer = input("Do you want to play the game of blackjack? 'y' for yes and 'n' for no: ")
            continue
        elif human_has_black_jack and computer_has_black_jack:
            isTie = True
            print("It's a Tie because you both have black jack")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
            answer = input("Do you want to play the game of blackjack? 'y' for yes and 'n' for no: ")
            continue
        elif computer_has_black_jack:
            computer_won = True
            print("You lost.")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
            answer = input("Do you want to play the game of blackjack? 'y' for yes and 'n' for no: ")
            continue
        
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while get_card == 'y':
            deal_card(human)
            ace_or_one(human)
            human_score = calculate_scores(human)
            print(f" Your cards are {human}, and current score is {human_score}")
            computer_draw(computer)
            ace_or_one(computer)
            computer_score = calculate_scores(computer)
            computer_first_card = reveal_first_card(computer)
            print(f"Computer's first card {computer_first_card}")

            if (human_score > 21 and computer_score > 21) or (human_score == computer_score):
                isTie = True
                break
            elif human_score > 21 or computer_score == 21:
                computer_won = True
                break
            elif computer_score > 21 or human_score == 21:
                human_won = True
                break
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_card == "n":
            computer_draw(computer)
            ace_or_one(computer)
            computer_score = calculate_scores(computer)
            
            if computer_score > 21 or human_score == 21 or human_score > computer_score:
                human_won = True
            elif computer_score > human_score or computer_score == 21:
                computer_won = True
            elif (human_score > 21 and computer_score > 21) or (human_score == computer_score):
                isTie = True
        
        if isTie:
            print("It's a tie. You both went over")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
        elif computer_won:
            print("You lost.")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
        elif human_won:
            print("You have won! Computer went over")
            print(f"Your final hand is {human}, and final score is {human_score}")
            print(f"computer's final hand is {computer}, final score is {computer_score}")
            
        
        answer = input("Do you want to play the game of blackjack? 'y' for yes and 'n' for no: ")

game()
        

    

    

  
        


            
        







    


    

    
    


    




