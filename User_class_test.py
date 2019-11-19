import unittest
from user_class import User

class MyTestCase(unittest.TestCase):
    def test_name(self):
        User1= User("Zubrah")
        self.assertEqual(User1.name, "Zubrah")

    def test_lname(self):
        User2 = User(87)
        self.assertNotEqual(User2.name, "Zubrah")

    def test_name3(self):
        User3 = User(1)
        self.assertAlmostEqual(User3.name, 1)

    def test_name4(self):
        User4 = User("Zubrah")
        self.assertTrue(User4.name, "Zebra")

    def test_name5(self):
        User5 =User("Ahmed")
        self.assertIs(User5.name, "Ahmed")



if __name__ == '__main__':
    unittest.main()
