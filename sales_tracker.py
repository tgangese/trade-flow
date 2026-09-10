sales = []
add_more = "yes"

while add_more == "yes":

    product = input(" Enter product: ")

    quantity = int(input("Enter quantity: "))

    price = int(input("Enter price: "))


    sale = {
        "product": product,
        "quantity": quantity,
        "price": price
    }

    sales.append(sale)

    add_more = input("Do you want to add another sale? yes/no: ")

total_revenue = 0

for sale in sales:
    total = sale["quantity"] * sale["price"]
    total_revenue = total_revenue + total

print("Total revenue", total_revenue)
