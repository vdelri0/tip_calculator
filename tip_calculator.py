print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
people = int(input("How many people to split the bill? #"))

tip_as_percentage = percentage * 0.001
tip = total * tip_as_percentage
bill_per_person = (total + tip)/people
split_value = round(bill_per_person, 2)
split_value = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${split_value}")