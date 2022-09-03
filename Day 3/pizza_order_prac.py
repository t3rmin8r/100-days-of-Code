# 🚨 Don't change the code below 👇
from ast import And
from audioop import add
from cgitb import small
from re import S
from tkinter import Y
from turtle import done


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_bill = 0

# Pizza Size base prices
S = 15
M = 20
L = 25

# ingredient pricing
pep_small = 2
pep_med_or_Large = 3
wants_extra_cheese = 1


#Calculate for inputs
# This is how I started, but wasn't working 
# After adding the Medium size so I knew the Large wouldn't work
# if size == "S":
#     total_bill += S
# if add_pepperoni == "Y":
#     total_bill += pep_small
# if extra_cheese == "Y":
#     total_bill += wants_extra_cheese

####Below is the start of the teacher explination####

if size == "S":
    total_bill += S
elif size == "M":
    total_bill += M
elif size == "L":
    total_bill += L

if add_pepperoni == "Y":
    if size == "S":
        total_bill += pep_small
    else:
        total_bill += pep_med_or_Large

if extra_cheese == "Y":
    total_bill += wants_extra_cheese


print(f"Your final bill is: ${total_bill}")
