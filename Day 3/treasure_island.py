print('''
*******************************************************************************
__________|                   |                  |                     |
__________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________|
__________|                `"=._o`"=._      _`"=._                     |
__________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
|_________|           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
__________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

which_way = input('You are at a crossroad. Which way do you want to go "L" or "R"?')
which_way = which_way.lower()
if which_way == "r":
    print("Game Over")
elif which_way == "l":
    lake_choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if lake_choice == "swim":
        print("Game Over")
    elif lake_choice == "wait":
        island_door_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue". Which colour do you choose?')
        if island_door_choice == "red" or island_door_choice == "blue":
            print("Game Over")
        elif island_door_choice == "yellow":
            print("You Win!")
        else:
            print("You done did it now!")