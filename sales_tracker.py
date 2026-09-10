#product = input("Enter product:")


#quantity = int(input("Enter quantity:"))


#price = int(input("Enter price"))



#sale = {

  #  "product": product,

  #  "quantity": quantity,

   # "price": price

#}


#total_sale_amount = sale["quantity"] * sale["price"]

#print("Total sale", total_sale_amount)
#print("product:",sale["product"])
#print("quantity:",sale["quantity"])
#print("price:",sale["price"])

sales = [
    {"product": "Beans", "quantity": 10, "price": 25000},
    {"product": "Rice", "quantity": 5, "price": 20000},
    {"product": "Garri", "quantity": 8, "price": 15000}
]

for sale in sales:
    total = sale["quantity"] * sale["price"]
    print(sale["product"]) 
    print("Total sale",total )

total_revenue = 0
for sale in sales:
    total = sale["quantity"] * sale["price"]
    total_revenue = total_revenue + total

print("Total revenue",total_revenue)