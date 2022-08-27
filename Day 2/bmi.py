# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# The line below we specify bmi as a variable 
# we convert weight and height to float incase there 
# are decimals. Then height is raised to the 2nd power.
# We then print the bmi as an integer so there are no decimals
bmi = float(weight) / float(height) ** 2
print(int(bmi))
#This line will print bmi rounded to two decimal places
print(round(bmi,2))


