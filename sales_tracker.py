sales = []
add_more = "yes"

while add_more == "yes":

    product = input(" Enter product: ")

    valid_quantity = False

    while not valid_quantity:

        try:
            quantity = int(input("Enter quantity: "))
            valid_quantity = True

        except:
            print("enter a valid number")

    valid_price = False

    while not valid_price:
        try:
            price = int(input("Enter price: "))
            valid_price = True

        except:
            print("enter a valid number")    

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
