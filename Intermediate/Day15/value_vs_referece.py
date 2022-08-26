
# pass by reference
#the exact same object is passed through reference
#a dictionary is a mutable object
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0.0
}

def change(res):
    res["water"] = "sprite"

change(resources)
print(resources)


#pass by value.
#a copy of the object is made in order to be used in the function
# an integer is an immutable object
money = 64
def change_mon(mon):
    mon -= 10

change_mon(money)
print(money)