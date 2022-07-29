import random
#a string of people's names
names_string = input("Give me everybody's names, separated by a comma. ")

#split the string into a list
names = names_string.split(",")

random_int=random.randint(0,len(names)-1)
print(names[random_int],"is going to buy the meal today")

#.choice
person=random.choice(names)
print(person,"is going to buy the meal today")