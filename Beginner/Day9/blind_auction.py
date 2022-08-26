

from pygments import highlight


def create_user_and_bid(username,bid,dic):
    if username not in dic:
        dic[username] = bid
    else:
        dic[username] = bid
    
    return dic

def get_highest_bid (dic):
    highest = 0
    for item in auction_dic:
        highest = max(highest,dic[item])
    return highest

def get_winner(dic):
    winner = ""
    highest = 0

    for person,money in auction_dic.items():
        if money > highest:
            highest = money
            winner = person

    return winner


auction_dic = {}
keep_going = True
while keep_going:
    name = input("What is your name? ")
    bid_dollar = int(input("What is your bid?: $ "))
    create_user_and_bid(name,bid_dollar,auction_dic)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    while more_bidders != "yes" and more_bidders != "no":
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if more_bidders == "no":
        keep_going = False
    elif more_bidders == "yes":
        keep_going == True

highest_bid = get_highest_bid(auction_dic)
bid_winner = get_winner(auction_dic)

print(f"The winner is {bid_winner} with a bid of ${highest_bid}")







        


