# I will make variables for the bill and tip in decimal form.
bill_bt = 250.00
tip = 0.15
tip_amt = bill_bt * tip
bill_w_tip = bill_bt + tip_amt

print("The tip on a $" + str(bill_w_tip) + " resturant bill is $" + str(tip_amt))
