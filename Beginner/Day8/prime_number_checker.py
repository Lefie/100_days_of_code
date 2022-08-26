
#a prime number only has two factors 

#Write your code below this line 👇


def prime_checker(number):
    if number == 1:
        return "1 is neither a prime number nor a composite number"
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        return "This number is not prime"
    else:
        return "This is a prime number"


def prime_checker_solution(number):
    is_prime = True
    for i in range(2,number): 
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
print(prime_checker(number=n))

