# 🚨 Don't change the code below 👇
from ast import And
from audioop import add
from cgitb import small
from re import S
from tkinter import Y


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
pep_medium = 3
pep_large = 3
extra_cheese = 1


#Calculate for inputs
if size == "S":
    total_bill += S

wants_pep = add_pepperoni
if wants_pep == "Y":
    total_bill += pep_small

wants_extra_cheese = extra_cheese
if wants_extra_cheese == "Y":
    total_bill += 
else:
    total_bill = total_bill
# if size == "M": 
#     total_bill += M
# if size == "L":
#     total_bill += L



print(f"Your final bill is: ${total_bill}")
