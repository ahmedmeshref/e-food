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

# rating for our service
service_rate = 0


def food_menu():
    print("---------------------- Food Menu ----------------------")
    index = 0
    for meal in food_list:
        item = Food(meal[0], meal[1], meal[2])
        print(str(index) + ".", str(item))
        index += 1


def drinks_menu():
    print("---------------------- Drinks Menu ----------------------")
    index = 0
    for drink in drink_list:
        item = Drink(drink[0], drink[1], drink[2])
        print(str(index) + ".", str(item))
        index += 1


def customer_order():
    global user
    name = input("What is your name? ")
    user = Customer(name)
    order_items = []
    meal = input("Do you want a meal? (yes or no): ")
    while meal == "yes":
        food_menu()
        selected_meal = int(input("Enter the number of selected meal: "))
        order_items.append([food_list[selected_meal][0], food_list[selected_meal][-1]])
        meal = input("Do you want another meal? (yes or no): ")
    drink = input("Do you want a drink? (yes or no): ")
    while drink == "yes":
        drinks_menu()
        selected_drink = int(input("Enter number of selected drink: "))
        order_items.append([drink_list[selected_drink][0], drink_list[selected_drink][-1]])
        drink = input("Do you want another drink? (yes or no): ")
    return customer_payment(order_items)


def customer_payment(order_items):
    global service_rate
    confirm, order_price = user.confirm_order(order_items)
    if confirm == "1":
        order_status= user.payments(order_price, visa_list, balance)
        service_rate = user.review()
        return order_status

    elif confirm == "3":
        return "Order canceled successfully"


print(customer_order())
