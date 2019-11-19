from Food import Food
from Drink import Drink
from customer_class import Customer

# list of food
# food_1 =  [name, description, price]
meat_burger = ["Meat Burger", "grilled meat burger with chips", 10]
chicken_burger = ["Chicken Burger", "grilled chicken burger with chips", 12]
chicken_stroganoff = ["chicken stroganoff", "chicken with rice and chips", 15]
kebab = ["kebab", "grilled meat with chips", 10]
food_list = [meat_burger, chicken_burger, chicken_stroganoff, kebab]

# list of drinks
# drink_1 = [name, description, price]
coffee = ["Coffee", "Black coffee", 5]
lemonade = ["Lemonade Juice", "Lemon juice", 5]
tea = ["Tea", "Black Tea", 5]
hot_chocolate = ["Hot chocolate", "Hot Extra black chocolate", 10]
water = ["Water", "pure safee water", 5]
drink_list = [coffee, lemonade, tea, hot_chocolate, water]

# list of visas in our system with the balance
visa_list = ["001", "002"]
balance = [2000, 4000]


def f_menu():
    print("---------------------- Food Menu ----------------------")
    print("   Name" + " " * 20 + "Price")
    index = 0
    for meal in food_list:
        item = Food(meal[0], meal[1], meal[2])
        item.food_menu(index)
        index += 1


def d_menu():
    print("---------------------- Drinks Menu ----------------------")
    print("   Name" + " " * 20 + "Price")
    index = 0
    for drink in drink_list:
        item = Drink(drink[0], drink[1], drink[2])
        item.drinks_menu(index)
        index += 1


def customer_order():
    global user
    name = input("What is your name? ")
    user = Customer(name)
    order_items = []
    meal = input("Do you want a meal? (1 for yes): ")
    while meal == "1":
        f_menu()
        selected_meal = int(input("Enter the number of selected meal: "))
        f_quantity = int(input("quantity: "))
        order_items.append([food_list[selected_meal][0], food_list[selected_meal][-1], f_quantity])
        meal = input("Do you want another meal? (1 for yes): ")
    drink = input("Do you want a drink? (1 for yes): ")
    while drink == "1":
        d_menu()
        selected_drink = int(input("Enter number of selected drink: "))
        d_quantity = int(input("quantity: "))
        order_items.append([drink_list[selected_drink][0], drink_list[selected_drink][-1], d_quantity])
        drink = input("Do you want another drink? (1 for yes): ")
    return customer_payment(order_items)



def customer_payment(order_items):
    order_price = user.confirm_order(order_items)
    confirm = input("--------------- Confirm your order -------------------\n"
                    "1. Confirm \n"
                    "2. Delete an item \n"
                    "3. cancel \n"
                    "Enter a number: ")
    while confirm == "2":
        deleted_item = int(input("Enter of the element to delete: "))
        del order_items[deleted_item]
        order_price = user.confirm_order(order_items)
        if len(order_items) == 0:
            return "Order canceled successfully"
        confirm = input("--------------- Confirm your order -------------------\n"
                        "1. Confirm \n"
                        "2. Delete an item \n"
                        "3. cancel \n"
                        "Enter a number: ")
    if confirm == "3":
        return "Order canceled successfully"
    order_status = user.payments(order_price, visa_list, balance)
    return order_status


print(customer_order())
