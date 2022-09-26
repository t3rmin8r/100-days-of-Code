# 🚨 Don't change the code below 👇


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# map[3] = map[2]
horizontal = int(position[0])
vertical = int(position[1])
if horizontal > len(map) or vertical > len(map):
    print(f"dumbo, pick numbers that line up with the squares!")
else:
    map[horizontal-1][vertical-1] = 'x'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")