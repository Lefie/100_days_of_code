
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


#say, enter 31, column 3 and row 13

map[int(position[1])-1][int(position[0])-1]="X"

print(f"{row1}\n{row2}\n{row3}")
