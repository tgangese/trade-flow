import json
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="TradeFlow API", description="AI Business OS for African SMEs - Built in Otukpo")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)
def load_data():
    with open("sales.json", "r") as f:
        sales = json.load(f)
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except:
        expenses = []
    return sales, expenses

def get_amount(s):
    # auto-detect amount field
    for key in ['total', 'amount', 'price', 'value', 'revenue', 'cost']:
        if key in s:
            return float(s[key])
    # if quantity * price
    if 'quantity' in s and 'price' in s:
        return float(s['quantity']) * float(s['price'])
    if 'qty' in s and 'price' in s:
        return float(s['qty']) * float(s['price'])
    return 0

def get_product_name(s):
    for key in ['product', 'item', 'name', 'product_name', 'item_name']:
        if key in s:
            return s[key]
    return "Unknown"

def get_summary():
    sales, expenses = load_data()
    total_revenue = sum(get_amount(s) for s in sales)
    total_expenses = sum(get_amount(e) for e in expenses) if expenses else 0
    profit = total_revenue - total_expenses
    profit_margin = (profit / total_revenue * 100) if total_revenue else 0

    product_totals = {}
    for s in sales:
        name = get_product_name(s)
        product_totals[name] = product_totals.get(name, 0) + get_amount(s)

    best_product = max(product_totals, key=product_totals.get) if product_totals else "Rice"
    best_amount = product_totals.get(best_product, 0)
    best_percent = (best_amount / total_revenue * 100) if total_revenue else 0

    highest_expense = "Salaries"
    if expenses:
        try:
            highest_expense = max(expenses, key=lambda x: get_amount(x))
            highest_expense = highest_expense.get('category', highest_expense.get('name', 'Salaries'))
        except:
            pass

    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "profit": profit,
        "profit_margin": profit_margin,
        "best_seller": best_product,
        "best_seller_amount": best_amount,
        "best_seller_percent": best_percent,
        "highest_expense": highest_expense,
        "total_sales": len(sales)
    }

@app.get("/")
def home():
    return {"message": "TradeFlow API live - from Otukpo to the world", "docs": "/docs"}

@app.get("/dashboard")
def dashboard():
    summary = get_summary()
    sales, _ = load_data()
    cat = {}
    for s in sales:
        name = get_product_name(s)
        cat[name] = cat.get(name, 0) + get_amount(s)
    return {"financials": summary, "categories": cat}

@app.get("/insights")
def insights():
    s = get_summary()
    return {
        "best_seller": f"{s['best_seller']} = {s['best_seller_amount']} ({s['best_seller_percent']:.2f}% of revenue)",
        "highest_expense": s['highest_expense'],
        "profit_margin": f"{s['profit_margin']:.2f}%",
        "advice": f"{s['best_seller']} drives {s['best_seller_percent']:.2f}% - stock more"
    }

@app.get("/ask")
def ask(question: str):
    s = get_summary()
    q = question.lower()
    if "stock" in q or "sell" in q or "best" in q:
        return {"question": question, "answer": f"Stock more {s['best_seller']} - it drives {s['best_seller_percent']:.2f}% of revenue (N{s['best_seller_amount']}).", "data": s}
    elif "profit" in q:
        return {"question": question, "answer": f"Profit is N{s['profit']} with {s['profit_margin']:.2f}% margin. Revenue N{s['total_revenue']}. Highest expense {s['highest_expense']}.", "data": s}
    else:
        return {"question": question, "answer": f"Revenue N{s['total_revenue']}, Profit N{s['profit']}. Best seller {s['best_seller']}. Ask about stock, profit, or expenses.", "data": s}