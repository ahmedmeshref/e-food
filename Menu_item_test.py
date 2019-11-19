import unittest
from Menu_item_class import MenuItem


class MyTestCase(unittest.TestCase):
    def test_foodname(self):
        Item_1 = MenuItem("Burger", "burger grilled", 5)
        self.assertEqual(Item_1.Item_name, "Burger")

    def test_foodprice(self):
        Item_1 = MenuItem("Burger", "burger grilled", 5)
        self.assertEqual(Item_1.Item_price, 5)

    def test_foodDescr(self):
        Item_1 = MenuItem("Burger", "burger grilled", 5)
        self.assertEqual(Item_1.item_description, "burger grilled")

    def test_upper(self):
        self.assertEqual('food'.upper(), 'FOOD')

    def test_lower(self):
        self.assertEqual('FOOD'.lower(), 'food')



if __name__ == '__main__':
    unittest.main()
