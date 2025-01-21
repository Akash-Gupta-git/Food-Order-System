menu = {
    'As' : 45,
    'Italy' : 450,
    'Dosa' : 390,
    'Sambhar': 350,
    'Samosa' : 59,
    'Pizza' : 290,
    'Chilly' : 260,
    'Momos' :  250
}
Total_price = 0 


print("\n\n\t\t------------WELCOME TO ORDER SYSTEM----------")
print("\n")
print("*****This is our order menu please choose your order :\n")
print(menu)


order_1 = input("\nTell me your 1st order: ").capitalize()
if order_1 in menu:
    Total_price += menu[order_1]  
    print(f"\tFood price is : ${Total_price}")
    again = input("\nDo you want to order anything more (Yes/No)? ").capitalize()
    if(again == 'Y' or again == 'Yes'):
        order_2 = input("Tell me your 2nd order : ").capitalize()
        if order_2 in menu:
            Total_price += menu[order_2]  
            print(f"\tFood price is  : ${menu[order_2]}")
            print(f"\tTotal price is : ${Total_price}")
            again = input("\nDo you want to order anything more (Yes/No)? ").capitalize()
            if(again == 'Y' or again == 'Yes'):
                order_3 = input("Tell me your 3nd order : ").capitalize()
                if order_3 in menu:
                    Total_price += menu[order_3]  
                    print(f"\t {order_3} Price is :",menu[order_3]) 
                    print("Okay ")
                    print(f"you ordered = {order_1}, {order_2}, {order_3}")
                    print("\tTotal Price so far:", Total_price)
                    
                elif(order_3 not in menu):
                    print("\nSorry this order is not in menu list") 
                    print(f"you ordered = {order_1}, {order_2}")
                    print("\tTotal Price so far:", Total_price)
            elif(again == 'N' or again == 'No'):
                print("Okay ")
                print(f"you ordered = {order_2}.")
                print("\tTotal Price so far:", Total_price)
                print("\n----Thanks for ordering Sir") 
            else:
                print("You entered wrong option (yes/No)...!")  
        elif(order_2 not in menu):
                print(f"\n'{order_2}'....! Your order out of menu card ")
                print("\tTotal Price so far:", Total_price)
                print("\n----Thanks for ordering Sir") 
        else:
            print("Order not found.....!")
    elif(again == 'N' or again == 'No'):
        print("Okay ")
        print(f"you ordered = {order_1}.")
        print("\tTotal Price so far:", Total_price)
        print("\n----Thanks for ordering Sir") 
    else:
        print("You entered wrong option (yes/No)...!")  
elif(order_1 is menu):
        print("your order out of menu card...!")   
else:
    print("Order not found..404...!")

print("\n\n\t\t------------ORDER SYSTEM COMPLETED----------")

##--------------------------------
## Store the student details in dictionary  by user input and display 

# student = {}
# S_Name = input("Enter student name : ")
# S_Name = input("Enter student name : ")
# S_Name = input("Enter student name : ")
# S_Name = input("Enter student name : ")
# S_Name = input("Enter student name : ")

