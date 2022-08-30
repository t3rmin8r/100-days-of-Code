# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# BMI = weight / (height ** 2)

# Gather Measurements
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


# Calculate 
BMI = weight / (height ** 2)

if BMI <= 18:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}, you are underweight.")
elif BMI <= 22:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}, you have a normal weight.")
elif BMI <= 28:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}, you are slightly overweight.")
elif BMI <= 33:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}, you are obese.")
elif BMI <= 40:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}, you are clinically obese.")
else:
    print(f"Your BMI is {'{:.2f}'.format(BMI)}Dead")

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

###### Below is what I modified and submitted to the lesson
# # Calculate 
# BMI = weight / (height ** 2)

# if BMI <= 18.5:
#     print(f"Your BMI is {round(BMI)}, you are underweight.")
# elif BMI <= 25:
#     print(f"Your BMI is {round(BMI)}, you have a normal weight.")
# elif BMI <= 30:
#     print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
# elif BMI <= 35:
#     print(f"Your BMI is {round(BMI)}, you are obese.")
# elif BMI > 35:
#     print(f"Your BMI is {round(BMI)}, you are clinically obese.")
# else:
#     print(f"Your BMI is {round(BMI)}, you are clinically obese.")