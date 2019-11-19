
# defining a MenuItem class
class MenuItem:
    def __init__(self, item_name, item_description, item_price):
        self.Item_name = item_name
        self.item_description = item_description
        self.Item_price = item_price

    def __str__(self):
        return self.Item_name + ': $' + str(self.Item_price)
