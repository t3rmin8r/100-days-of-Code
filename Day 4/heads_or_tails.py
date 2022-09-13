#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇


### Here is the basic form and correct. Above is confusing not necessary
#


heads = 1
tails = 0
toss = random.randint(0, 1)


if toss == 0:
    print("Tail")
else:
    print("Heads")


