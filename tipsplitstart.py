# If the bill was $200.00, split between 5 people, with 12% tip.
# Each person should pay (200.00 / 5) * 1.12 = 44.80
# Round the result to 2 decimal places = 44.80

# Example: What is the total bill? 124.65
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay $19.93

# Example: What is the total bill? 124.65
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay $19.93

# Helpful hints for your final amount  round() #https://www.programiz.com/python-programming/methods/built-in/round

print('This is a tip calculator.\n')
# Step 1: Ask user input how many people and create variable and store # of people called people.

party = int(input('How many people are in your party?\n'))

# Step 2: Ask user input what is the bill amount. Create and store variable called bill.
bill = float(input('How much is your bill?\n'))

# Step 3: Ask user input on how much they want to tip. Create and store variable called tip.
tip = float(input('What is your tip amount? 10 to 20 is recommended.\n'))

# Step 4: Do the math
split = ((bill * (tip/100)) + bill) / party
each = round(split, 2)

# Step 5: Print out the message that should say what each owes.
if party < 2:
    print(f'Your total is ${each}.')
else:
    print(f'Each person owes ${each}.')
