# Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.
# The owner wants you to do some calculations on the data with these criteria's:
#     -calculate the total price average for all products
#     -create a new price list that reduces the old prices by $ 5
#     -calculate the total revenue generated from the products
#     -calculate the average daily revenue generated from the products
#     -based on the new prices, which products are less than $ 30 
# Below is the data you are to use for the problem :
# products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
# prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
# last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#calculate the total price average for all products
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

total_price_avg = calculate_average(prices)
print("The total price average for all products is ${}".format(round(total_price_avg)))

#create a new price list that reduces the old prices by $ 5
new_prices = [x-5 for x in prices]
print("New Prices List: {}".format(new_prices))

#calculate the total revenue generated from the products
def calculate_revenue(prices, quantities):
    assert len(prices) == len(quantities), "There must be an equal number of prices and quantities"
    return sum([p*q for p, q in zip(prices, quantities)])

total_revenue = calculate_revenue(prices, last_week)
print("Total Revenue Generated: ${}".format(round(total_revenue)))

#calculate the average daily revenue generated from the products
daily_revenue = calculate_revenue(new_prices, last_week)
daily_rev_per_day = daily_revenue/len(last_week)
print("Average Daily Revenue Generated per Day: ${}".format(round(daily_rev_per_day, 2)))

#based on the new prices, which products are less than $ 30?
less_than_30 = [product < 30 for product in new_prices]
if True:
    print("\nProducts Less Than $30:")
    for i in range(len(less_than_30)):
        if less_than_30[i]:
            print("{}: ${}".format(products[i], round(new_prices[i], 2)))
            

