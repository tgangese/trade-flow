from fastapi import FastAPI
import json
from sales_tracker import (
    calculate_total_revenue,
    calculate_total_expenses,
    calculate_profit,
    calculate_profit_margin,
    calculate_cash_flow,
    calculate_sales_per_product,
    most_expensive_category,
    best_selling_product
)

app = FastAPI(title="TradeFlow API - SME Business OS")

def load_data():
    with open("sales.json", "r") as f:
        sales = json.load(f)
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
    return sales, expenses

@app.get("/")
def home():
    return {"message": "TradeFlow API running", "mission": "AI Business OS for African SMEs"}

@app.get("/dashboard")
def dashboard():
    sales, expenses = load_data()
    total_revenue = calculate_total_revenue(sales)
    total_expenses = calculate_total_expenses(expenses)
    profit = calculate_profit(sales, expenses)
    margin = calculate_profit_margin(profit, total_revenue)
    cash_flow = calculate_cash_flow(sales, expenses)
    best_prod, best_amt = best_selling_product(sales)
    high_cat, high_amt = most_expensive_category(expenses)
    
    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "profit": profit,
        "profit_margin": round(margin, 2),
        "cash_flow": cash_flow,
        "best_seller": {"product": best_prod, "amount": best_amt},
        "highest_expense": {"category": high_cat, "amount": high_amt},
        "total_sales": len(sales)
    }

@app.get("/insights")
def insights():
    sales, expenses = load_data()
    product_sales = calculate_sales_per_product(sales)
    total_rev = calculate_total_revenue(sales)
    
    insights_list = []
    best_prod, best_amt = best_selling_product(sales)
    if best_prod:
        pct = (best_amt / total_rev * 100) if total_rev else 0
        insights_list.append(f"{best_prod} drives {pct:.1f}% of revenue - consider stocking more")
    
    high_cat, high_amt = most_expensive_category(expenses)
    if high_cat:
        insights_list.append(f"Highest cost is {high_cat} at {high_amt} - review for savings")
    
    return {"insights": insights_list, "product_breakdown": product_sales}