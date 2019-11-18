from user_class import User

class Customer(User):
    def confirm_order(self, orders):
        index = 0
        total_money = 0
        print("--------------- Your Order -------------------")
        for item in orders:
            print(str(index) + ".", item[0], ":", item[1])
            total_money += item[1]
            index += 1
        confirm = input("--------------- Confirm your order -------------------\n"
                        "1. Confirm \n"
                        "2. Delete an item \n"
                        "3. cancel \n"
                        "Enter a number: ")
        if confirm == "2":
            delete_element = input("Enter number of the element to delete: ")
            # to complete tomorrow
        return confirm, total_money

    def payments(self, order_price, visa_list, balance):
        visa = input("Enter your visa number: ")
        if visa in visa_list:
            if order_price <= balance[visa_list.index(visa)]:
                return "Order placed successfully"
            else:
                return "No sufficient balance"

    # def review(self):
    #     review_rate = input("How many starts you rate the service (out of 5): ")
    #     return review_rate
