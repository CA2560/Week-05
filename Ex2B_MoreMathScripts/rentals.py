people = int(input("How many people are attending the tour? "))

charter_van = 15
van_costs = 250

needed_vans = people / charter_van
total_cost = needed_vans * van_costs
print(total_cost)
split_costs = total_cost / people
print(split_costs)

print(f"You will need {round(needed_vans)} vans to transport {people} people.")
print(f"The total cost of the vans will be ${total_cost:.2f}.")
print(f"Each person will pay ${split_costs:.2f} for the van rental.")

# the script said to charge 16.67 per person.
# multiplying by 38, the result is 633.46
# the vans were 633.33
# I believe that the left over is from the rounding of the vans needed. 