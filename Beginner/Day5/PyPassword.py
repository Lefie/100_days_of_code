#Password Generator Project
import random
#random.choice
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
,'z',]

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','#','$','%',"&",'(',')','*','+']

print("Welcome to the PyPassword Generator!")

nr_letter=int(input("How many letters would you like in your password?\n"))

nr_symbols=int(input("How many symbols would you like?"))

nr_numbers=int(input("How many numbers would you like?"))

password=""

len_of_pass=nr_letter+nr_numbers+nr_symbols

letter=""
for i in range(nr_letter):
   letter+=letters[random.randint(0,len(letters)-1)]


symbol=""
for i in range(nr_symbols):
   symbol+=symbols[random.randint(0,len(symbols)-1)]


nums=""
for i in range(nr_numbers):
   nums+=numbers[random.randint(0,len(numbers)-1)]

password=letter+symbol+nums
#print(password)
a_list=list(password) #convert the password string into a list

mixed=""
for x in range(len(a_list)):
    random_word=a_list[random.randint(0,len(a_list)-1)] #pick a random char
    mixed+=random_word #add it to the empty string
    a_list.remove(random_word) #remove the random word

print("Here is your password:",mixed)


#could use random.shuffle()


