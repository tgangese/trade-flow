import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TradeFlow API - Otukpo to World - Groq Free AI")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

def load_data():
    with open("sales.json","r") as f: sales=json.load(f)
    try:
        with open("expenses.json","r") as f: expenses=json.load(f)
    except: expenses=[]
    return sales, expenses

def get_amount(s):
    for k in ['total','amount','price','value','revenue','cost']:
        if k in s: return float(s[k])
    return 0

def get_product_name(s):
    for k in ['product','item','name','product_name']:
        if k in s: return s[k]
    return "Unknown"

def get_summary():
    sales, expenses = load_data()
    total_revenue = sum(get_amount(s) for s in sales)
    total_expenses = sum(get_amount(e) for e in expenses) if expenses else 0
    profit = total_revenue-total_expenses
    profit_margin = (profit/total_revenue*100) if total_revenue else 0
    product_totals={}
    for s in sales:
        name=get_product_name(s)
        product_totals[name]=product_totals.get(name,0)+get_amount(s)
    best = max(product_totals, key=product_totals.get) if product_totals else "Corn"
    best_amount = product_totals.get(best,0)
    best_percent = (best_amount/total_revenue*100) if total_revenue else 0
    highest = "Salaries"
    if expenses:
        try:
            h=max(expenses, key=lambda x: get_amount(x))
            highest=h.get('category',h.get('name','Salaries'))
        except: pass
    return {"total_revenue":total_revenue,"total_expenses":total_expenses,"profit":profit,"profit_margin":profit_margin,"best_seller":best,"best_seller_amount":best_amount,"best_seller_percent":best_percent,"highest_expense":highest,"total_sales":len(sales),"product_breakdown":product_totals}

@app.get("/")
def home(): return {"message":"TradeFlow API v1.1 - Groq Free AI live - Otukpo","docs":"/docs","ask":"/ask?question=wetin I suppose stock"}

@app.get("/dashboard")
def dashboard():
    s=get_summary()
    return {"financials":s,"categories":s['product_breakdown']}

@app.get("/insights")
def insights():
    s=get_summary()
    return {"best_seller":f"{s['best_seller']} = {s['best_seller_amount']} ({s['best_seller_percent']:.2f}%)","profit_margin":f"{s['profit_margin']:.2f}%","advice":f"{s['best_seller']} drives {s['best_seller_percent']:.2f}% - stock more"}

@app.get("/ask")
def ask(question: str):
    s=get_summary()
    q=question.lower()
    groq_key=os.getenv("GROQ_API_KEY")
    # Try Groq FREE first
    if groq_key:
        try:
            from groq import Groq
            client=Groq(api_key=groq_key)
            system_prompt=f"""You are TradeFlow AI for Nigerian market traders in Otukpo. Speak simple English + small Pidgin, short, friendly, actionable under 3 sentences.

Data: Revenue ₦{s['total_revenue']}, Profit ₦{s['profit']} ({s['profit_margin']:.1f}% margin), Expenses ₦{s['total_expenses']}, Sales {s['total_sales']}, Best Seller {s['best_seller']} ₦{s['best_seller_amount']} ({s['best_seller_percent']:.1f}%), Highest Expense {s['highest_expense']}, Products {s['product_breakdown']}

If ask wetin to stock -> recommend best seller with %. If profit low -> mention expenses. Use Naira and Pidgin like 'Na Your Gain', 'Make You Stock Am' when natural."""
            resp=client.chat.completions.create(model="openai/gpt-oss-120b", messages=[{"role":"system","content":system_prompt},{"role":"user","content":question}], max_tokens=200, temperature=0.7)
            ans=resp.choices[0].message.content.strip()
            return {"question":question,"answer":ans,"data":s,"ai":"groq-llama3-free"}
        except Exception as e:
            print(f"Groq error: {e} falling back")
           
    # Fallback rules (never fails)
    if any(k in q for k in ["stock","sell","best","wetin"]):
        return {"question":question,"answer":f"Make You Stock Am: {s['best_seller']} - it drives {s['best_seller_percent']:.2f}% of revenue (₦{s['best_seller_amount']}). Na your best seller!","data":s,"ai":"rules"}
    elif any(k in q for k in ["profit","gain"]):
        return {"question":question,"answer":f"Na Your Gain: Profit ₦{s['profit']} with {s['profit_margin']:.2f}% margin. Revenue ₦{s['total_revenue']}. Highest expense na {s['highest_expense']}.","data":s,"ai":"rules"}
    else:
        return {"question":question,"answer":f"Revenue ₦{s['total_revenue']}, Profit ₦{s['profit']}. Best seller {s['best_seller']} ({s['best_seller_percent']:.1f}%). Ask about wetin to stock or profit.","data":s,"ai":"rules"}
