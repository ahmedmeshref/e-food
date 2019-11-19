from Food import Food
from Drink import Drink
from customer_class import Customer
from super_user_class import SuperUser

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

# list of super users with their respective passwords
user_name = ["ahmed", "mohamed"]
user_password = ["000", "111"]


# defining food menu function
def f_menu():
    print("---------------------- Food Menu ----------------------")
    print("   Name" + " " * 20 + "Price")
    index = 0
    for meal in food_list:
        item = Food(meal[0], meal[1], meal[2])
        item.food_menu(index)
        index += 1
    print("--------------------------------------------------------")


# defining drink menu function
def d_menu():
    print("---------------------- Drinks Menu ----------------------")
    print("   Name" + " " * 20 + "Price")
    index = 0
    for drink in drink_list:
        item = Drink(drink[0], drink[1], drink[2])
        item.drinks_menu(index)
        index += 1
    print("----------------------------------------------------------")


# Customer control flow
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


# defining customer payment function
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


# Super user control flow

# editing a price of an existing item
def edit_food_price():
    f_menu()
    food_to_edit = int(input("Select a food number: "))
    new_price = int(input("New price:"))
    food_list[food_to_edit][-1] = new_price
    print("Price updated successfully")


# defining editing drinking from the list
def edit_drink_price():
    d_menu()
    drink_to_edit = int(input("Select a drink number: "))
    new_price = int(input("New price:"))
    drink_list[drink_to_edit][-1] = new_price
    print("Price updated successfully")


# defining a function to add new food to the list
def add_new_food():
    meal_name = input("Meal name:")
    meal_description = input("Meal description: ")
    meal_price = int(input("Price: "))
    food_list.append([meal_name, meal_description, meal_price])
    print(meal_name, "added successfully")


# function to add new drink to the list
def add_new_drink():
    drink_name = input("Meal name:")
    drink_description = input("Meal description: ")
    drink_price = int(input("Price: "))
    drink_list.append([drink_name, drink_description, drink_price])
    print(drink_name, "added successfully")


# function to delete a food from the available list
def delete_food():
    f_menu()
    food_to_delete = int(input("Enter the number of item: "))
    del food_list[food_to_delete]
    print("Item deleted successfully")


# function to delete a drink from the available list
def delete_drink():
    d_menu()
    drink_to_delete = int(input("Enter the number of item: "))
    del drink_list[drink_to_delete]
    print("Item deleted successfully")


# function to view food and drink items
def view_items():
    f_menu()
    d_menu()


# superuser function
def super_user_menu():
    print("---------------------- Menu ----------------------")
    selected_action = input("1- View all items\n"
                            "2- Edit food price     3- Edit drink price\n"
                            "4- Add new food        5- Add new drink\n"
                            "6- Delete food         7- Delete drink\n"
                            "Select a number: ")
    if selected_action == "1":
        view_items()
    elif selected_action == "2":
        edit_food_price()
    elif selected_action == "3":
        edit_drink_price()
    elif selected_action == "4":
        add_new_food()
    elif selected_action == "5":
        add_new_drink()
    elif selected_action == "6":
        delete_food()
    else:
        delete_drink()


# log_in validation
def validate():
    user_1 = SuperUser("User")
    validation = user_1.log_in(user_name, user_password)
    while validation == 0:
        validation = user_1.log_in(user_name, user_password)
    super_user_menu()


# Main menu to order for customers or log in for super_user
user_type = input("1- Order \n"
                  "2- Log in (Owner) \n"
                  "Select a choice number to proceed: ")

if user_type == "1":
    print(customer_order())
else:
    validate()
    run_again = input("Do you want another operation? (1 for yes): ")
    while run_again == "1":
        super_user_menu()
