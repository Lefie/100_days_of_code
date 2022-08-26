"""
This program is testing to see if a given year is a leap year

a leap year is evenly divisible by 4
EXCEPT a year that is evenly divisible by 100
Unless the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))
"""
# One way of doing it 
is_leap=True
count=0
if year%4==0:
    is_leap
    count+=1
else:
    count+=0

if year%100==0:
    is_leap=False
    count+=0
else:
    count+=1

if year%400==0:
    is_leap
    count+=1
else:
    count+=0

if count>=2:
    print("It's a leap year")
else:
    print("Not a leap year")

"""

if year%4!=0:
    print("Not a leap year")
elif year%100==0:
    print("Not a leap year")
elif year %400==0:
    print("A leap year")
else:
    print("Not a leap year")






