import art

#calculator functionalities
#Add
def add (a,b):
    return a+b


#Subtract 
def subtract(a,b):
    return a-b


#Multiply
def multiply(a,b):
    return a*b

#Divide 
def divide(a,b):
    return a/b


#create a dictionary to store the operations 
operation_dic ={}
operation_dic["+"] = add
operation_dic["-"] =subtract
operation_dic["*"] = multiply
operation_dic["/"] = divide

#function = operation_dic["*"]
#print(function(2,3))
def calculator():
    print(art.logo)
    num1 = float(input("What is the first number? "))
    should_continue = True
    for operation in operation_dic:
        print(operation)

    while should_continue:
        num2 = float(input("What is the second number? "))

        operation_symbol = input("pick an operation from above: ")

        function = operation_dic[operation_symbol]
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        proceed = input("Type 'y' to continue and 'n' to exit, 'f' for fresh start " )

        if proceed == "y":
            num1 = answer
        elif proceed == "f":
            should_continue = False
            calculator()
        else:
            print("Thank you for choosing this calculator. Goodbye")
           
            break

calculator()
    


