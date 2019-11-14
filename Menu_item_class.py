class MenuItem:
    def __init__(self, item_name, item_price,item_ratings):
        self.Item_name = item_name
        self.Item_price = item_price
        self.Item_ratings = item_ratings


    def info(self):
        return self.Item_name + ': $' + str(self.Item_price)

    def get_total_price(self, count):
        total_price = self.Item_price * count
        return round(total_price)
