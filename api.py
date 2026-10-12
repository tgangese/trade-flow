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
            resp=client.chat.completions.create(model="qwen/qwen3-32b", messages=[{"role":"system","content":system_prompt},{"role":"user","content":question}], max_tokens=200, temperature=0.7)
            ans=resp.choices[0].message.content.strip()
            if not ans or len(ans) < 10:
                ans = f"My oga, for Christmas promo — Make You Stock Am: {s['best_seller']} (₦{s['best_seller_amount']}, {s['best_seller_percent']:.1f}% of revenue) and Garri. Na your gain be ₦{s['profit']} with {s['profit_margin']:.1f}% margin!"
            return {"question":question,"answer":ans,"data":s,"ai":"groq-llama3-free"}
        except Exception as e:
            print(f"Groq error: {e} falling back")