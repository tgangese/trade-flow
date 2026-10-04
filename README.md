# TradeFlow - AI Business OS for African SMEs

Built from Otukpo, Benue State for market traders who need offline-first business intelligence.

## What it does

TradeFlow turns messy sales books into instant business decisions.

Terminal:

=== TradeFlow - SME Dashboard ===
Financial Summary

Total Revenue: 12454640
Profit: 12315740.0
Profit Margin: 98.88%
Best seller: Rice - 5010000 (40.23% of revenue)
Highest expense: Salaries - 50000
Code


API:
```bash
GET /dashboard
→ {"total_revenue":12454640, "best_seller": {"product":"Rice","amount":5010000}}

GET /insights
→ ["Rice drives 40.2% of revenue - consider stocking more"]

Architecture

    Data Layer: JSON persistence with validation (82 sales tracked)
    Calculation Layer: Revenue, expenses, profit, margin, cash flow, zero-division safe
    Analytics Layer: Most expensive category, best seller, product breakdown
    UX Layer: Interactive menu (modular flows, not 300-line dump)
    API Layer: FastAPI with /dashboard, /insights, auto docs at /docs

Run locally
Bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Terminal OS
python3 sales_tracker.py

# API OS
uvicorn api:app --reload
# Open http://127.0.0.1:8000/docs


Roadmap

    Financial Management (daily, range, cash flow)[x]
    Business Intelligence (best seller, highest expense)[x]
    API Layer (FastAPI)[x]
    RAG Assistant - "Why is my profit low?" → AI uses real data
    WhatsApp Bot - traders query via WhatsApp
    Frontend Dashboard - React calling /dashboard

Why this matters

African SMEs lose 60% of profit to poor tracking. TradeFlow is offline-first, API-ready, and AI-extensible - built for Otukpo market realities, scalable to 44M Nigerian SMEs.

Stack: Python, FastAPI, JSON, Git - AI Engineer foundations.
Code


Then:

```bash
git add README.md
git commit -m "Add README - TradeFlow AI Business OS narrative"
git push

