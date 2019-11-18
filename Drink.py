from Menu_item_class import MenuItem

class Drink(MenuItem):
    def drinks_menu(self, index):
        print(str(index) + ".", self.Item_name, " " * (22 - len(self.Item_name)),self.Item_price)

