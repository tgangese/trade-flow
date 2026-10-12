import json
import os
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
    for key in ['total', 'amount', 'price', 'value', 'revenue', 'cost']:
        if key in s:
            return float(s[key])
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

    best_product = max(product_totals, key=product_totals.get) if product_totals else "Corn"
    best_amount = product_totals.get(best_product, 0)
    best_percent = (best_amount / total_revenue * 100) if total_revenue else 0

    highest_expense = "Salaries"
    if expenses:
        try:
            highest = max(expenses, key=lambda x: get_amount(x))
            highest_expense = highest.get('category', highest.get('name', 'Salaries'))
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
        "total_sales": len(sales),
        "product_breakdown": product_totals
    }

@app.get("/")
def home():
    return {"message": "TradeFlow API live - from Otukpo to the world - v1.1 AI", "docs": "/docs"}

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

    # --- Try REAL OpenAI if key exists ---
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)

            system_prompt = f"""
You are TradeFlow AI, a business advisor for Nigerian market women in Otukpo.
Speak simple English + small Pidgin, short, actionable, friendly.

Real business data:
- Total Revenue: ₦{s['total_revenue']}
- Profit (Na Your Gain): ₦{s['profit']} ({s['profit_margin']:.1f}% margin)
- Total Expenses: ₦{s['total_expenses']}
- Total Sales Count: {s['total_sales']}
- Best Seller: {s['best_seller']} = ₦{s['best_seller_amount']} ({s['best_seller_percent']:.1f}% of revenue)
- Highest Expense: {s['highest_expense']}
- All Products: {s['product_breakdown']}

Rules:
- Use real numbers to advice
- If they ask "wetin I suppose stock" -> recommend best seller with %
- If profit low -> explain expenses
- Keep answer under 3 sentences, mention Naira
- Mix Pidgin like "Na Your Gain", "Make You Stock Am" when natural
"""
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                max_tokens=150,
                temperature=0.7
            )
            ai_answer = resp.choices[0].message.content.strip()
            return {"question": question, "answer": ai_answer, "data": s, "ai": "openai"}
        except Exception as e:
            print(f"OpenAI error: {e}, falling back to rules")
            # fall through to rule-based

    # --- Fallback rule-based (works without key) ---
    if "stock" in q or "sell" in q or "best" in q or "wetin" in q:
        return {"question": question, "answer": f"Make You Stock Am: {s['best_seller']} - it drives {s['best_seller_percent']:.2f}% of revenue (₦{s['best_seller_amount']}). Na your best seller!", "data": s, "ai": "rules"}
    elif "profit" in q or "gain" in q:
        return {"question": question, "answer": f"Na Your Gain: Profit is ₦{s['profit']} with {s['profit_margin']:.2f}% margin. Revenue ₦{s['total_revenue']}. Highest expense na {s['highest_expense']}.", "data": s, "ai": "rules"}
    else:
        return {"question": question, "answer": f"Revenue ₦{s['total_revenue']}, Profit ₦{s['profit']}. Best seller {s['best_seller']} ({s['best_seller_percent']:.1f}%). Ask me about wetin to stock or why profit high/low.", "data": s, "ai": "rules"}