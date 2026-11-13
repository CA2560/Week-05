# looking up the rule of 72, I will make a variable for the rate and amount of money
# to be doubled.
bank_acc = 10000
ir = 4
time_to_double = 72 / ir
time_with_rate = 72/ time_to_double

worth = bank_acc * (1 + (time_with_rate / 100)) ** time_to_double
print(int(worth))

print("Your current savings is $" + str(float(bank_acc)))
print("at a " + str(ir) + "% interest rate, your savings account will be")
print("worth $" + str(int(worth)) + " in " + str(int(time_to_double)) + " years.")

# Had to look up the formula for the total ammount of money to be doubled with interest.
