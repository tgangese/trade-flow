import json

# Function to get a positive number (used for quantity and price)
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

# Function to get a valid product name (non-empty, normalized)
def get_product(prompt):
    valid_product = False
    while not valid_product:
        product = input(prompt).strip().capitalize()
        if product == "":
            print("Product cannot be empty.")
        else:
            valid_product = True
    return product

# Load existing sales from sales.json
with open("sales.json", "r") as file:
    sales = json.load(file)

add_more = "yes"

# Main loop to add sales
while add_more == "yes":

    # Get product, quantity, and price using functions
    product = get_product("Enter product: ")
    quantity = get_positive_number("Enter quantity: ")
    price = get_positive_number("Enter price: ")

    # Create sale dictionary and add to list
    sale = {
        "product": product,
        "quantity": quantity,
        "price": price
    }
    sales.append(sale)

    # Ask if user wants to add another sale
    add_more = ""
    while add_more != "yes" and add_more != "no":
        add_more = input("Do you want to add another sale? yes/no: ").strip().lower()

# Function to calculate total revenue
def calculate_total_revenue(sales):
    total_revenue = 0
    for sale in sales:
        total = sale["quantity"] * sale["price"]
        total_revenue += total
    return total_revenue

# Function to display each sale with labels
def display_sales(sales):
    print("Sales:")
    for sale in sales:
        total = sale["quantity"] * sale["price"]
        print(sale["product"], "— Quantity:", sale["quantity"], "— Price:", sale["price"], "— Total:", total)

# Display all sales
display_sales(sales)

# Function call to calculate and store total revenue
total_revenue = calculate_total_revenue(sales)

# Display total revenue
print("Total revenue:", total_revenue)

# Save updated sales back to sales.json
sales_json = json.dumps(sales)
with open("sales.json", "w") as file:
    file.write(sales_json)
