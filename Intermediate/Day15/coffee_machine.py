# 3 flavors of coffee : espresso, latte, cappucino

# coins : pennym nickel, dime and quarter

"""
Program Requirements
1. print report 
2. resources sufficient?
3. process coins 
4. check transaction successful?
5. make coffee if successful. 
"""




import resource


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0.0
}


QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01





def print_report(resources):
    count = 0
    for item,value in resources.items():
        if count < 2:
            print(f"{item}: {value}ml" )
            count += 1
        elif count == 2:
            print(f"{item}: {value}g" )
            count += 1
        else:
            print(f"{item}:${value}")

def check_sufficient_resources(resources,answer,menu):
    is_sufficient = True
    ingredient_dic = menu[answer]["ingredients"]

    for key in ingredient_dic.keys(): #if the keys in the ingredients also are present in resources, check if we have enoguh
        if key in resources:
            if ingredient_dic[key] <= resources[key] and ingredient_dic[key]>= 0 and resources[key] >= 0 : #if ingredient requirement is smaller than the resources, we have enough 
                is_sufficient = True 
            else:
                is_sufficient = False
                print(f"Sorry there is not enough {key}")
                break
    
    if is_sufficient == True :
        return True 
    else:
        return False 

def process_coins(quarter,dime,nickel,penny):
    total_q = quarter * QUARTER 
    total_d = dime * DIME
    total_n = nickel * NICKEL
    total_p = penny * PENNY

    total = round((total_q + total_d + total_n + total_p),2 )
    return total 



def transaction_success(answer,money_entered,menu):
    is_success = False
    cost_to_pay = menu[answer]['cost']
    if money_entered >= cost_to_pay:
        is_success = True
    else:
        print("Sorry that's not enough money. Money refunded ")
        is_success = False
    return is_success

def return_money(money_entered,answer,menu):
    charge = 0
    if money_entered > menu[answer]['cost']:
        charge = money_entered - menu[answer]['cost']
    
    return charge 





def update_report(resources,answer,menu):
    ingredient_dic = menu[answer]['ingredients']
    for key in ingredient_dic:
        if key in resources:
            resources[key] -= ingredient_dic[key]
    
    resources['money'] += menu[answer]['cost']
    


makeCoffee = True 
while makeCoffee == True :
    answer = input("What drink would you like? (espresso/latte/cappuccino)")

    if answer == "off":
        print("Stopping")
        makeCoffee = False
        break


    if answer == "report":
        print_report(resources)
    
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if check_sufficient_resources(resources,answer,MENU):
            enter_quarter = int(input("How many quarters? "))
            enter_dime = int(input("How many dimes? "))
            enter_nickel = int(input("How many nickels? "))
            enter_penny= int(input("How many pennies? "))
        else:
            print("Not enough resources")
            continue


        money_entered = process_coins(enter_quarter,enter_dime,enter_nickel,enter_penny)

        if transaction_success(answer,money_entered,MENU):
            if money_entered > MENU[answer]['cost']:
                charge = return_money(money_entered,answer,MENU)
                print(f"Here is ${charge} dollars in change")
            update_report(resources,answer,MENU)
            print_report(resources)
        else:
            print("Go get a job")
        






