# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
import random
from secrets import choice
from tkinter import N
from unicodedata import name


# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "todd, scott, tracy, tabby, logan, alyssa"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# print(names)
# len_names = len(names) - 1
if "joe" in names:
    names.remove("joe")
# if pick eq joe ---remove joe and pick again
u_choice = random.randint(0, len(names) - 1)
print(f"{names[u_choice]} is going to buy the meal today")




# if u_choice == 6:
#     print("I picked joe, lol")
#     u_choice = random.randint(0, len(names) - 1)



### Working Code Below
# numb_names = len(names)
# random_choice = random.randint(0, numb_names - 1)
# who_pays = names[random_choice]

# print(f"{who_pays} will pay the bill!")