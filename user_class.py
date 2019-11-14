class User(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print("welcome to our e-food, have a nice meal", self.name)
    def view_menu(self):
        pass