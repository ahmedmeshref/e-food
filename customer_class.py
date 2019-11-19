from user_class import User

# Defining Customer class
class Customer(User):
    def confirm_order(self, orders):
        index = 0
        total_money = 0
        print("--------------- Your Order -------------------")
        print(" Item Name", " " * 15, "Quantity"," " * 8, "Price ($)")

        for item in orders:
            print(str(index) + ".", item[0], ":", " " * (20 - len(item[0])), item[2], " " * 15, item[1] * item[2])
            total_money += item[1]
            index += 1
        print("Total :", str(total_money) + "$")
        return total_money

    def payments(self, order_price, visa_list, balance):
        visa = input("Enter your visa number: ")
        if visa in visa_list:
            if order_price <= balance[visa_list.index(visa)]:
                return "Order placed successfully"
            else:
                return "No sufficient balance"
