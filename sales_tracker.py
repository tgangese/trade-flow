import json
from datetime import date, datetime

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

def get_valid_date(prompt):
    while True:
        date_text = input(prompt)

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")

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

def find_sales_by_product(sales, target_product):
    matching_sales = []

    for sale in sales:
        if sale["product"] == target_product:
            matching_sales.append(sale)

    return matching_sales

def calculate_today_revenue(sales):
    total_revenue = 0
    today = date.today().isoformat()

    for sale in sales:
        if sale["date"] == today:
            total = sale["quantity"] * sale["price"]
            total_revenue += total

    return total_revenue

def calculate_today_sales(sales):
    today_sales = 0
    today = date.today().isoformat()

    for sale in sales:
        if sale["date"] == today:
            today_sales += 1
    return today_sales
def find_sales_by_date(sales, target_date):
    matching_sales = []

    for sale in sales:
        if sale["date"] == target_date:
            matching_sales.append(sale)

    return matching_sales

def get_non_empty_text(prompt, label="Item"):
    while True:
        text = input(prompt).strip().capitalize()

        if text == "":
            print(f"{label} cannot be empty.")
        else:
            return text

def find_sales_by_date_range(sales, start_date, end_date):
    matching_sales = []

    for sale in sales:
        if start_date <= sale["date"] <= end_date:
            matching_sales.append(sale)

    return matching_sales

def expenses_report(sales, expenses):
    total_expenses = 0

    for expense in expenses:
        print(expense["category"], "-", expense["amount"])
        total_expenses += expense["amount"]

    print("Total expenses:", total_expenses)

    category_totals = calculate_expenses_per_category(expenses)

    print("Expenses by category:")
    for category, total in category_totals.items():
        print(category, "-", total)

    total_revenue = calculate_total_revenue(sales)

    profit = calculate_profit(sales, expenses)
    print("Profit:", profit)

    profit_margin = calculate_profit_margin(profit, total_revenue)
    print(f"Profit Margin: {profit_margin:.2f}%")

def add_expense(expenses):
    category = get_non_empty_text("Enter expense category: ", "Expense category")
    amount = get_positive_number("Enter expense amount: ")
    expense = {
        "category": category,
        "amount": amount,
        "date": date.today().isoformat()
    }

    expenses.append(expense)


def calculate_expenses_per_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = expense["amount"]
        else:
            category_totals[category] += expense["amount"]

    return category_totals

def calculate_profit(sales, expenses):
    total_revenue = calculate_total_revenue(sales)
    total_expenses = calculate_total_expenses(expenses)

    profit = total_revenue - total_expenses

    return profit

def calculate_profit_margin(profit, revenue):
    profit_margin = (profit / revenue) * 100
    return profit_margin

def financial_summary(sales, expenses):
    total_revenue = calculate_total_revenue(sales)
    total_expenses = calculate_total_expenses(expenses)
    profit = calculate_profit(sales, expenses)
    profit_margin = calculate_profit_margin(profit, total_revenue)

    print("Financial Summary")
    print("-----------------")
    print("Total Revenue:", total_revenue)
    print("Total Expenses:", total_expenses)
    print("Profit:", profit)
    print(f"Profit Margin: {profit_margin:.2f}%")

def calculate_total_expenses(expenses):
    total_expenses = 0

    for expense in expenses:
        total_expenses += expense["amount"]

    return total_expenses

def find_expenses_by_date(expenses, target_date):
    matching_expenses = []

    for expense in expenses:
        if expense["date"] == target_date:
            matching_expenses.append(expense)

    return matching_expenses


def financial_summary_by_date(sales, expenses, target_date):
    daily_sales = find_sales_by_date(sales, target_date)
    daily_expenses = find_expenses_by_date(expenses, target_date)

    total_revenue = calculate_total_revenue(daily_sales)
    total_expenses = calculate_total_expenses(daily_expenses)

    profit = total_revenue - total_expenses
    profit_margin = calculate_profit_margin(profit, total_revenue)

    return total_revenue, total_expenses, profit, profit_margin

def financial_summary_by_date_range(sales, expenses, start_date, end_date):
    period_sales = find_sales_by_date_range(sales, start_date, end_date)

    period_expenses = find_expenses_by_date_range(
        expenses, start_date, end_date
    )

    total_revenue = calculate_total_revenue(period_sales)
    total_expenses = calculate_total_expenses(period_expenses)

    profit = total_revenue - total_expenses
    profit_margin = calculate_profit_margin(profit, total_revenue)

    return total_revenue, total_expenses, profit, profit_margin


def find_expenses_by_date_range(expenses, start_date, end_date):
    matching_expenses = []

    for expense in expenses:
        if start_date <= expense["date"] <= end_date:
            matching_expenses.append(expense)

    return matching_expenses

# Function to generate sales report
def sales_report(sales):
    total_sales = len(sales)
    print("Total sales:", total_sales)

    total_revenue = calculate_total_revenue(sales)
    today_revenue = calculate_today_revenue(sales)
    today_sales = calculate_today_sales(sales)

    # New feature: product search
    target_product = get_product("Enter product: ")
    matching_sales = find_sales_by_product(sales, target_product)
    if len(matching_sales) == 0:
        print(f"No sales found for {target_product}")
    else:
        display_sales(matching_sales)
        product_revenue = calculate_total_revenue(matching_sales)
        print(f"Total revenue for {target_product}: ₦{product_revenue:,}")

    target_date = get_valid_date("Enter date (YYYY-MM-DD): ")
    matching_sales = find_sales_by_date(sales, target_date)

    if len(matching_sales) == 0:
        print(f"No sales found for {target_date}")
        date_revenue = 0
    else:
        display_sales(matching_sales)
        print("Number of sales:", len(matching_sales))
        date_revenue = calculate_total_revenue(matching_sales)

    # Date-range search
    while True:
        start_date = get_valid_date("Enter start date (YYYY-MM-DD): ")
        end_date = get_valid_date("Enter end date (YYYY-MM-DD): ")

        if start_date > end_date:
            print("Start date cannot be after end date.")
        else:
            break

    matching_range_sales = find_sales_by_date_range(sales, start_date, end_date)

    if len(matching_range_sales) == 0:
        print(f"No sales found between {start_date} and {end_date}")
        range_revenue = 0
    else:
        display_sales(matching_range_sales)
        print("Number of sales:", len(matching_range_sales))
        range_revenue = calculate_total_revenue(matching_range_sales)

    print("Revenue from", start_date, "to", end_date, ":", range_revenue)

    max_sale = 0
    max_product = ""

    for sale in sales:
        total = sale["quantity"] * sale["price"]
        if total > max_sale:
            max_sale = total
            max_product = sale["product"]

    print("Total revenue:", total_revenue)
    print("Today's revenue:", today_revenue)
    print("Today's sales:", today_sales)
    print("Revenue for", target_date, ":", date_revenue)
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
        print("sales per product: No revenue")

if __name__ == "__main__":
    # Load existing sales from sales.json
    with open("sales.json", "r") as file:
        sales = json.load(file)

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

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
            add_more = input(
                "Do you want to add another sale? yes/no: "
            ).strip().lower()

    # Display all sales
    display_sales(sales)

    # Save updated sales back to sales.json
    sales_json = json.dumps(sales)
    with open("sales.json", "w") as file:
        file.write(sales_json)

    # Call the report function
    sales_report(sales)

    add_expense(expenses)

    expenses_json = json.dumps(expenses)
    with open("expenses.json", "w") as file:
        file.write(expenses_json)

    expenses_report(sales, expenses)
    financial_summary(sales, expenses)

    target_date = get_valid_date("Enter date for financial summary (YYYY-MM-DD): ")

    daily_revenue, daily_expenses, daily_profit, daily_profit_margin = financial_summary_by_date(
        sales, expenses, target_date
    )

    print("Daily revenue:", daily_revenue)
    print("Daily expenses:", daily_expenses)
    print("Daily profit:", daily_profit)
    print("Daily profit margin:", f"{daily_profit_margin:.2f}%")

    start_date = get_valid_date("Enter start date for financial summary (YYYY-MM-DD): ")
    end_date = get_valid_date("Enter end date for financial summary (YYYY-MM-DD): ")

    range_revenue, range_expenses, range_profit, range_profit_margin = financial_summary_by_date_range(
        sales, expenses, start_date, end_date
    )

    print("Financial Summary for", start_date, "to", end_date)
    print("----------------------------------------")
    print("Revenue:", range_revenue)
    print("Expenses:", range_expenses)
    print("Profit:", range_profit)
    print("Profit Margin:", f"{range_profit_margin:.2f}%")
