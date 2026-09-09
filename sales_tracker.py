product = input("Enter product:")


quantity = int(input("Enter quantity:"))


price = int(input("Enter price"))



sale = {

    "product": product,

    "quantity": quantity,

    "price": price

}

total_sale_amount = sale["quantity"] * sale["price"]

print("Total sale", total_sale_amount)