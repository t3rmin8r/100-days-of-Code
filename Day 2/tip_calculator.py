# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00/5) * 1.12
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

# inputs from the user
bill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 15, 18, or 20? "))
peep_count = int(input("How many people are splitting the bill? "))

# perform the math for the tip percentage 
tip_perc = perc / 100
tip_total = tip_perc * bill
total_bill = bill + tip_total
ea_party_pays = total_bill / peep_count

# rounding 
total_bill = round(total_bill, 2)
# ea_party_pays = round(ea_party_pays, 2)


print(f"The total bill with tip is ${total_bill}")
print(f"The total bill for each party is ${round(ea_party_pays, 2)}")
