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

def calculate_cash_flow(sales, expenses):
    total_revenue = calculate_total_revenue(sales)
    total_expenses = calculate_total_expenses(expenses)
    return total_revenue - total_expenses

def calculate_profit_margin(profit, revenue):
    if revenue == 0:
        return 0.0
    profit_margin = (profit / revenue) * 100
    return profit_margin


def financial_summary(sales, expenses):
    total_revenue = calculate_total_revenue(sales)
    total_expenses = calculate_total_expenses(expenses)
    profit = calculate_profit(sales, expenses)
    profit_margin = calculate_profit_margin(profit, total_revenue)
    cash_flow = calculate_cash_flow(sales, expenses)

    print("Financial Summary")
    print("-----------------")
    print("Total Revenue:", total_revenue)
    print("Total Expenses:", total_expenses)
    print("Profit:", profit)
    print(f"Profit Margin: {profit_margin:.2f}%")
    print("Cash Flow:", cash_flow)

    expensive_cat, expensive_amount = most_expensive_category(expenses)
    if expensive_cat:
        print(f"Highest expense: {expensive_cat} - {expensive_amount}")

    best_product, best_amount = best_selling_product(sales)
    if best_product:
        total_revenue = calculate_total_revenue(sales)
        percentage = (best_amount / total_revenue * 100) if total_revenue else 0
        print(f"Best seller: {best_product} - {best_amount} ({percentage:.2f}% of revenue)")


def calculate_total_expenses(expenses):
    total_expenses = 0

    for expense in expenses:
        total_expenses += expense["amount"]

    return total_expenses

def most_expensive_category(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    if not category_totals:
        return None, 0

    most_expensive = max(category_totals, key=category_totals.get)
    return most_expensive, category_totals[most_expensive]


def best_selling_product(sales):
    product_sales = calculate_sales_per_product(sales)
    
    if not product_sales:
        return None, 0
    
    best_product = max(product_sales, key=product_sales.get)
    return best_product, product_sales[best_product]


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

    cash_flow = calculate_cash_flow(daily_sales, daily_expenses)

    return total_revenue, total_expenses, profit, profit_margin, cash_flow

def financial_summary_by_date_range(sales, expenses, start_date, end_date):
    period_sales = find_sales_by_date_range(sales, start_date, end_date)
    period_expenses = find_expenses_by_date_range(expenses, start_date, end_date)

    total_revenue = calculate_total_revenue(period_sales)
    total_expenses = calculate_total_expenses(period_expenses)

    profit = total_revenue - total_expenses
    profit_margin = calculate_profit_margin(profit, total_revenue)
    cash_flow = calculate_cash_flow(period_sales, period_expenses)

    return total_revenue, total_expenses, profit, profit_margin, cash_flow

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

def add_sale_flow(sales):
    add_more = "yes"
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
    with open("sales.json", "w") as file:
        json.dump(sales, file)
    print(f"Saved. Total sales: {len(sales)}")

def add_expense_flow(expenses):
    add_expense(expenses)
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expense saved.")

def search_flow(sales):
    target_product = get_product("Enter product to search: ")
    matching = find_sales_by_product(sales, target_product)
    if not matching:
        print(f"No sales for {target_product}")
    else:
        display_sales(matching)
        print(f"Revenue for {target_product}: ₦{calculate_total_revenue(matching):,}")

if __name__ == "__main__":
    with open("sales.json", "r") as file:
        sales = json.load(file)
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    for sale in sales:
        if "date" not in sale:
            sale["date"] = date.today().isoformat()

    while True:
        print("\n=== TradeFlow - SME Dashboard ===")
        print("1. Add Sale")
        print("2. Add Expense")
        print("3. View Dashboard (Financial Summary + Insights)")
        print("4. Search Sales by Product")
        print("5. Search Sales by Date")
        print("6. View All Sales")
        print("7. View Expenses Report")
        print("8. Exit")
        
        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            add_sale_flow(sales)
        elif choice == "2":
            add_expense_flow(expenses)
        elif choice == "3":
            financial_summary(sales, expenses)
        elif choice == "4":
            search_flow(sales)
        elif choice == "5":
            d = get_valid_date("Enter date (YYYY-MM-DD): ")
            m = find_sales_by_date(sales, d)
            if not m:
                print(f"No sales for {d}")
            else:
                display_sales(m)
                print(f"Total for {d}: {calculate_total_revenue(m)}")
        elif choice == "6":
            display_sales(sales)
            print(f"Total sales: {len(sales)}")
        elif choice == "7":
            expenses_report(sales, expenses)
        elif choice == "8":
            print("Goodbye! TradeFlow saved.")
            break
        else:
            print("Invalid choice.")