

import math
def paint_calc(height = 1,width = 1,cover = 1):
    area = height * width 
    cove = math.ceil(area / cover )
    print("rounding",cove)

    return cove


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_area = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You will need {paint_area} cans of paint")

