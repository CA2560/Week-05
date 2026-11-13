# looking up the rule of 72, I will make a variable for the rate and amount of money
# to be doubled.
bank_acc = int(input("What is the amount of money in your savings account? "))
ir = 4
time_to_double = 72 / ir
time_with_rate = 72/ time_to_double

worth = bank_acc * (1 + (time_with_rate / 100)) ** time_to_double

print(f"Your current savings is $, {str(format(bank_acc, '.2f'))}")
print(f"at a {str(ir)}% interest rate, your savings account will be")
print(f"worth ${str(format(worth, '.2f'))} in {str(int(time_to_double))} years.")

# Had to look up the formula for the total ammount of money to be doubled with interest.
# adding in input function can have issues arise with data types and cause an error in the code when executing.
# I would have to convert the input function into an interger for the code to work. 