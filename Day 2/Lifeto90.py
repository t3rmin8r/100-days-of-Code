# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# My attempt
##### year = [365,52,12]
##### life = 18

##### days = year[0]
##### weeks = year[1]
##### months = year[2]

##### while x <= life:
#####     print(f"You have {days}")

# Instructor Code
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
