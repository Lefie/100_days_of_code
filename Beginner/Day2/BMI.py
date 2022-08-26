"""
BMI=weight(kg)/height^2(m^2)

"""

def calculate_BMI():

    weight=input("What is your weight in kg?")
    height=input("What is your height in meters?")

    BMI=int(float(weight)/(float(height)**2))
    return BMI

#Testing

print(calculate_BMI())