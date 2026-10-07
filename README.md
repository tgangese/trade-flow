# TradeFlow - AI Business OS for African SMEs
Built in Otukpo, Benue State 🇳🇬 — From messy sales books to AI decisions.

🚀 **LIVE:**
- **Frontend (for traders):** https://trade-flow-7xa5-chi.vercel.app/
- **API:** https://trade-flow-brw1.onrender.com
- **API Docs:** https://trade-flow-brw1.onrender.com/docs
- **Ask AI Example:** https://trade-flow-brw1.onrender.com/ask?question=stock

📊 **Real Data:** 81 sales | ₦498,740 revenue | ₦360,140 profit (72.2%) | Best Seller: Corn (12% of revenue)

For market women — profit is "Na Your Gain", advice is "Make You Stock Am"

## What It Does

TradeFlow turns messy paper sales books into instant business decisions for African SMEs.

**Terminal OS:**
=== TradeFlow - SME Dashboard ===
Total Revenue: ₦498,740
Profit (Na Your Gain): ₦360,140
Margin: 72.2%
Best Seller: Corn - ₦60,000 (12.03%) — Make You Stock Am

Code

**API OS:**
```bash
GET /dashboard → {revenue, profit, margin, best_seller}
GET /insights → {advice, product_breakdown}
GET /ask?question=stock → "Corn drives 12% - stock more"

1 line hidden
Frontend OS: Mobile-first dashboard for mama traders — no laptop needed.

Architecture
Data Layer: JSON persistence, validation, 81 sales tracked
Calculation Layer: Revenue, expenses, profit, margin, cash flow (zero-division safe)
Analytics Layer: Best seller, highest expense, product mix
UX Layer: Interactive terminal + mobile web
API Layer: FastAPI with CORS, /docs auto-generated
Deploy Layer: Render (API) + Vercel (Frontend) — Otukpo to World

Run Locally
Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Terminal
python3 sales_tracker.py

# API
uvicorn api:app --reload
# → http://127.0.0.1:8000/docs

Roadmap
Financial Management (daily, range, cash flow)[x]
Business Intelligence (best seller, highest expense)[x]
API Layer (FastAPI + CORS)[x]
Frontend for market women (Vercel live)[x]
Deployment (Render + Vercel)[x]
 RAG Assistant — real OpenAI for Pidgin queries
 WhatsApp Bot — traders query via WhatsApp
 Auth & Multi-trader support

Why This Matters
African SMEs lose 60% of profit to poor tracking. TradeFlow is offline-first, API-ready, AI-extensible — built for Otukpo market realities, scalable to 44M Nigerian SMEs.

Stack: Python, FastAPI, Vercel, Render, Git — AI Engineer foundations.
Builder: @tgangese — Building AI for Naija from Otukpo.


Save `Ctrl+O` → Enter → `Ctrl+X`

Then:

```bash
git add README.md
git commit -m "TradeFlow v1.0 FINAL - Live links brw1 + 7xa5, 81 sales, 360k profit, roadmap updated"
git push