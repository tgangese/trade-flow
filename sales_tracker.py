def get_positive_number(prompt):
    valid_number = False
    while not valid_number:
        try:
            number = int(input(prompt))
            if number > 0:
                valid_number = True
                return number
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

sales = []
add_more = "yes"

while add_more == "yes":
    product = ""
    while product == "":
        product = input("Enter product: ")
        product = product.strip().capitalize()
        if product == "":
            print("Product cannot be empty.")

    # Use the function for quantity and price
    quantity = get_positive_number("Enter quantity: ")
    price = get_positive_number("Enter price: ")

    sale = {
        "product": product,
        "quantity": quantity,
        "price": price
    }
    sales.append(sale)

    add_more = ""

    while add_more != "yes" and add_more != "no":
        add_more = input("Do you want to add another sale? yes/no: ").strip().lower()

# Calculate total revenue
total_revenue = 0
for sale in sales:
    total = sale["quantity"] * sale["price"]
    total_revenue += total

print("Total revenue:", total_revenue)
