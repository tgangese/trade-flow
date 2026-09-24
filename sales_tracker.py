import json
from datetime import date
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
        print(sale["product"], "— Quantity:", sale["quantity"], "— Price:", sale["price"], "— Total:", total, "— Date:", sale["date"])
# Function to calculate sales per product
def calculate_sales_per_product(sales):
    product_sales = {}
    for sale in sales:
        total = sale["quantity"] * sale["price"]
        if sale["product"] not in product_sales:
            product_sales[sale["product"]] = total
        else:
            product_sales[sale["product"]] += total
    return product_sales

def calculate_today_revenue(sales):
    total_revenue = 0
    today = date.today().isoformat()

    for sale in sales:
        if sale["date"] == today:
            total = sale["quantity"] * sale["price"]
            total_revenue += total

    return total_revenue
# Function to generate sales report
def sales_report(sales):
    total_sales = len(sales)
    print("Total sales:", total_sales)

    total_revenue = calculate_total_revenue(sales)
    today_revenue = calculate_today_revenue(sales)
    max_sale = 0
    max_product = ""

    for sale in sales:
        total = sale["quantity"] * sale["price"]
        if total > max_sale:
            max_sale = total
            max_product = sale["product"]

    print("Total revenue:", total_revenue)
    print("Today's revenue:", today_revenue)
    print("Highest sale:", max_product, "—", max_sale)

    if total_sales > 0:
        average_sale = total_revenue / total_sales
        print("Average sale:", round(average_sale, 2))
    else:
        print("Average sale: No sales")

    if total_sales > 0:
        min_sale = sales[0]["quantity"] * sales[0]["price"]
        min_product = sales[0]["product"]

        for sale in sales:
            total = sale["quantity"] * sale["price"]
            if total < min_sale:
                min_sale = total
                min_product = sale["product"]

        print("Lowest sale:", min_product, "—", min_sale)
    else:
        print("Lowest sale: No sales")

    # New feature: sales per product
    product_sales = calculate_sales_per_product(sales)

    if total_revenue > 0:
        print("Sales per product:")
        for product, total in product_sales.items():
            percentage = total / total_revenue * 100
            print(product, "—", total, f"({round(percentage, 2)}%)")
    else:
        print("Sales per product: No revenue")
# Load existing sales from sales.json
with open("sales.json", "r") as file:
    sales = json.load(file)

for sale in sales:
    if "date" not in sale:
        sale["date"] = date.today().isoformat()

add_more = "yes"

# Main loop to add sales
while add_more == "yes":
    product = get_product("Enter product: ")
    quantity = get_positive_number("Enter quantity: ")
    price = get_positive_number("Enter price: ")

    sale = {
        "product": product,
        "quantity": quantity,
        "price": price,
        "date": date.today().isoformat()
    }
    sales.append(sale)

    add_more = ""
    while add_more != "yes" and add_more != "no":
        add_more = input("Do you want to add another sale? yes/no: ").strip().lower()

# Display all sales
display_sales(sales)

# Save updated sales back to sales.json
sales_json = json.dumps(sales)
with open("sales.json", "w") as file:
    file.write(sales_json)

# Call the report function
sales_report(sales)
