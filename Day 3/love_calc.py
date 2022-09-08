# 🚨 Don't change the code below 👇
from itertools import count
from operator import truediv


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


joined_names = name1 + name2
lower_names = joined_names.upper()

true_count = lower_names.count("T")
true_count = true_count + lower_names.count("R")
true_count = true_count + lower_names.count("U")
true_count = true_count + lower_names.count("E")

true_love = lower_names.count("L")
true_love = true_love + lower_names.count("O")
true_love = true_love + lower_names.count("V")
true_love = true_love + lower_names.count("E")

# true_count = true_count
# love_score = L + O + V + E



combined_score = str(true_count)+str(true_love)
combined_score = int(combined_score)

if combined_score < 10 or combined_score > 90:
    print(f"Your score is {combined_score}, you go together like coke and mentos.")
elif combined_score > 40 or combined_score < 50:
    print(f"Your score is {combined_score}, you are alright together.")
else:
    print(f"Your score is {combined_score}")

