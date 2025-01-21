menu = {
    'As': 45,
    'Dosa': 390,
    'Italy': 450,
    'Pizza': 290,
    'Sambhar': 350,
    'Samosa': 59,
    'Chilly': 260,
    'Momos': 250
}

def menuCalling(**kwargs):
    for key, value in kwargs.items():
        print(key, "\t\t:", value)

def customer():
    print("--------------------------Please fill the form first.-------------------\n")
    customer_name = input("\nEnter your name: \t")
    customer_address = input("Enter your Address: \t")
    print("\n-----------------------------Form Closed-------------------------------------\n")
    return {"Name": customer_name, "Address": customer_address}

def take_order():
    total_price = 0
    order_list = []
    while True:
        order = input("\nTell me your order: ").capitalize()
        if order in menu:
            total_price += menu[order]
            order_list.append(order)
            print(f"\tAdded '{order}' to your order. Price: ${menu[order]}")
        else:
            print(f"\nSorry, '{order}' is not available in the menu.")

        again = input("\nDo you want to order anything more (Yes/No)? ").capitalize()
        if again == 'No' or again == 'N':
            break
    return total_price, order_list

# Main Program
print("\n\n\t\t------------WELCOME TO ORDER SYSTEM----------")
print("\n*****This is our order menu, please choose your order:\n")
menuCalling(**menu)

customer_details = customer()
print("\nCustomer Details:")
for key, value in customer_details.items():
    print(f"{key}: {value}")

print("\nHello! How can I help you, sir?")
total_price, order_list = take_order()

print("\n----Order Summary----")
print("Items Ordered:", ", ".join(order_list))
print("Total Price: $", total_price)
print("\n----Thanks for ordering! Visit again!----")


print("\n\n\t\t------------ORDER SYSTEM COMPLETED----------")













