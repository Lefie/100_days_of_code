#an empty dictionary 
empty_dic ={}

empty_dic["Bug"] = "An error in the program"
empty_dic["Loop"] = "The action of doing something over and over again"

#modify values
empty_dic["Bug"] = "Not a real bug. It is an error in the program"

#loop through a dictionary 
for key,value in empty_dic.items():
    print(key,":",value)