"""
Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.


"""

# .lower()
#.count(" ")

name1=input("What is your name?")

name2=input("What is their name?")

new_name1=name1.lower()

new_name2=name2.lower()




count_t=new_name1.count("t")
count_t2=new_name2.count("t")
print("T occurs",count_t+count_t2,"times")

count_r=new_name1.count("r")
count_r2=new_name2.count("r")
print("R occurs",count_r+count_r2,"times")

count_u=new_name1.count("u")
count_u2=new_name2.count("u")
print("U occurs",count_u+count_u2,"times")

count_e=new_name1.count("e")
count_e2=new_name2.count("e")
print("E occurs",count_e+count_e2,"times")


count_l=new_name1.count("l")
count_l2=new_name2.count("l")
print("L occurs",count_l+count_l2,"times")

count_o=new_name1.count("o")
count_o2=new_name2.count("o")
print("O occurs",count_o+count_o2,"times")

count_v=new_name1.count("v")
count_v2=new_name2.count("v")
print("V occurs",count_v+count_v2,"times")

count_e=new_name1.count("e")
count_e2=new_name2.count("e")
print("E occurs",count_e+count_e2,"times")


sum_of_true=count_t+count_t2+count_r+count_r2+count_u+count_u2+count_e+count_e2



sum_of_love=count_l+count_l2+count_o+count_o2+count_v+count_v2+count_e2+count_e


total_sum=int(str(sum_of_true)+str(sum_of_love))

if total_sum<10 or total_sum>90:
    print(f"Your score is {total_sum},you go together like cake and mentos")
elif total_sum>40 and total_sum<50:
    print(f"Your score is {total_sum},you are alright together")
else:
    print(f"Your score is {total_sum}")
