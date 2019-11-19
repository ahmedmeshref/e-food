from Menu_item_class import MenuItem


# defining a food class
class Food(MenuItem):
    def food_menu(self, index):
        print(str(index) + ".", self.Item_name, " " * (22 - len(self.Item_name)), self.Item_price)
