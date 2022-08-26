"""
Scope
"""
#predict result 
#example 1
enemies = 1
def increase_enemies ():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies() #what is the result ?
print(f"enemires outside function: {enemies}") #the global variable is not changed


#example 2 : global variable can be printed from insdide or outside the function. but not local variables
apple_color = "red"
def pick_apples():
    num_of_apples = 5
    print(f"This is inside a funciton. there are {num_of_apples} apples and the color of the apple is {apple_color}")

print("This is outside the funciton. apple color is ",apple_color)

"""
try:
    print(num_of_apples)
except:
    print("printing num_of_apples will cause an error because num_of_apples is a local variable")
"""
    
#example 3
color_of_lemon = "yellow"
if color_of_lemon == "yellow":
    new_color = "green" # we created a new variable here but since it's not inside a function, it is still valid 

def color_function():
    if color_of_lemon == "yellow":
        new_color = "red"
color_function()
print(new_color)

#example 4: Modifying a global variable. 

color_of_sky = "blue"
num_of_stars = 5

def change_color():
    global color_of_sky #this is not a recommended way because it causes bugs 
    color_of_sky = "grey"

def change_color2():
    return "dark"

print(color_of_sky)
change_color()
print(color_of_sky)
color_of_sky = change_color2()
print(color_of_sky)

# example 5: global constants 
PI = 3.14159

def cal():
    return PI 