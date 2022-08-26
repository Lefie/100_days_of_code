import game_data
import random

def generate_new_samples():

    #generate a random number between 0 and 49 
    random_num1 = random.randint(0,49)
    random_num2 = random.randint(0,49)
    #choose 2 samples
    sampleA = game_data.data[random_num1]
    sampleB = game_data.data[random_num2]

    return sampleA,sampleB
   

def description(sample):
    name = sample['name']
    detail = sample['description']
    origin = sample['country']
    string = name + ", a " + detail + ", from " + origin 
    return string 

#return True if sample 1 is bigger 
def compare(sample1,sample2):
    if sample1['follower_count'] > sample2['follower_count']:
        return True 
    else:
        return False


isTrue = True
score = 0
while isTrue:
    sampleA,sampleB = generate_new_samples()

    print('Compare A: ', description(sampleA))
    print('VS')
    print('Compare B: ', description(sampleB))


    answer = input("Who has more followers ? Type 'A' or 'B' ")

    result = compare(sampleA,sampleB)
    if result == True:
        if answer == 'A':
            score += 1 
            print(f"You've got it right. Your score is {score}")
        elif answer == 'B':
            print(f"You lost. your score is {score}")
            isTrue = False
            break
    else:
        if answer == 'B':
            score += 1
            print(f"You've got it right. Your score is {score}")

        elif answer == 'A':
            print(f"You lost. your score is {score}")
            isTrue = False
            break


        


   




