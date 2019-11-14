from Menu_item_class import MenuItem


class Food(MenuItem):
    def __init__(self,item_name,item_price,item_ratings):
        super().__init__(item_name, item_price, item_ratings)


    def info(self):
        return self.Item_name + ': $' + str(self.Item_price) + ' (' + str(self.Item_ratings


