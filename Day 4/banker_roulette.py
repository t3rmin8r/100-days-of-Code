# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_names = random.names
print(num_names)

### Working Code Below
# numb_names = len(names)
# random_choice = random.randint(0, numb_names - 1)
# who_pays = names[random_choice]

# print(f"{who_pays} will pay the bill!")