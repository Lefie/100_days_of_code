
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_result=round(weight/height**2)


if bmi_result<18.5:
    print("Your BMI is",bmi_result,"You are underweight!")
elif bmi_result<25:
    print("Your BMI is",bmi_result,"You are at normal weight!")
elif bmi_result<30:
    print("Your BMI is",bmi_result,"You are slightly overweight")
elif bmi_result<35:
    print("Your BMI is",bmi_result,"You are obese")
else:
    print("Your BMI is",bmi_result,"You are clinically obese")

