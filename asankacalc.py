charge = input("Enter the charge for the food: ")

tip = 18/100 * float(charge) #calculates the tip
#print(tip)
tip_dollars = "${:.2f}".format(tip)
print("Tip = " + str(tip_dollars))

tax = 7/100 * float(charge) #calculates sales tax
#print(tax)
tax_dollars = "${:.2f}".format(tax)
print("Sales tax = " + str(tax_dollars))

total_cost = float(charge) + float(tip) + float(tax) #adds up the total bill
cost_dollars = "${:.2f}".format(total_cost)
print("Grand total = " + str(cost_dollars)) 
