# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00/5) * 1.12
# Round the result to 2 decimal places = 33.60


print("Welcome to the tip calculator!")
bill = float(input("What is the cost of the whole bill? $"))
tip = float(input("What is the amount of the tip? 10, 12, 15, 20? "))
friend_count = int(input("How many friends are splitting the bill? "))
tip_asa_percent = tip / 100
tip_amount = tip_asa_percent * bill
total_bill = tip_amount + bill
ea_friend_pays = total_bill / friend_count
formatted_bill = "{:.2f}".format(ea_friend_pays)
print(f"Each Friend Pays ${formatted_bill}")