shopping_cart = []
store_name = ""

#Get the name of the store from the user
store_name = input("Enter the name of the store: ")

while True:
    #Display menu options
    print("\n1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View items in cart")
    print("4. Calculate total")
    print("5. Exit")

    #user to input menu choice
    option = input("Enter your choice (1-5): ")

    if option == "1": #Add item to the cart
        item_name = input("Enter the name of the item: ")

        #validate and get a numerical value
        while True:
            try:
                quantity = int(input("Enter the quantity: "))
                price = float(input("Enter the price per unit: KES"))
                break
            except ValueError:
                print("Error: Please enter a numerical value." )

        shopping_cart.append({"name": item_name, "quantity": quantity, "price": price})#adds items to the cart
        print(f"{item_name} added to the cart.") #shortcut to format, that way item name is picked automatically

    elif option == "2": #remove item from cart
        item_to_remove= input("Enter the name of the item to remove: ")
        found = False
        for item in shopping_cart:
            if item["name"] == item_to_remove:
                shopping_cart.remove(item)
                found = True
                print(f"{item_to_remove} removed from the cart.")
                break
            if not found:
                print(f"{item_to_remove} is not in the cart.")

    elif option == "3": #view cart's contents
        print(f"\nItems in your shopping cart from {store_name}:")
        for item in shopping_cart:
            print(f"{item['name']}: KES{item['price']}, {item['quantity']}piece(s)")

    elif option == "4": #calculate and display the total cost
        total_cost = sum([item['price'] * item['quantity'] for item in shopping_cart])
        print(f"\nTotal Cost: KES{total_cost}")

    elif option == "5": #exit
        print("\nThank you for using our service! Goodbye!\n\n")
        break

    else: #handle any invalid choices
        print("\nInvalid choice.\nPlease choose again.")



