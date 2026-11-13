monthly_income = int(input("What is your monthly income? "))
fed_taxes = 0.23
fed_tax_amount = monthly_income * fed_taxes
print(f"Your federal tax amount is: ${fed_tax_amount:.2f}")
yearly_fed_withholding = fed_tax_amount * 12
print(f"Your yearly federal withholding is: ${yearly_fed_withholding:.2f}")