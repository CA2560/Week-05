corporation = 10000000
real_estate = 34000000
assests = corporation + real_estate
loan = 2500000
gov_fees = 1000000
debt = loan + gov_fees
net_worth = assests - debt

print("your total assests are: $" + str(assests))
print("your total debts are: $" + str(debt))
print("your net worth is: $" + str(net_worth))