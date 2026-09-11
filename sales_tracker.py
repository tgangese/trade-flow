sales = []
add_more = "yes"

while add_more == "yes":

    product = input("Enter product: ")

    # Quantity validation
    valid_quantity = False
    while not valid_quantity:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                valid_quantity = True
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid number for quantity.")

    # Price validation
    valid_price = False
    while not valid_price:
        try:
            price = int(input("Enter price: "))
            if price > 0:
                valid_price = True
            else:
                print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid number for price.")

    # Create sale dictionary
    sale = {
        "product": product,
        "quantity": quantity,
        "price": price
    }
    sales.append(sale)

    add_more = input("Do you want to add another sale? yes/no: ")

# Calculate total revenue
total_revenue = 0
for sale in sales:
    total = sale["quantity"] * sale["price"]
    total_revenue += total

print("Total revenue:", total_revenue)
