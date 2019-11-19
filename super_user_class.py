from user_class import User


# defining a SuperUser class
class SuperUser(User):
    def log_in(self, user_name, user_password):
        user_name_input = input("Enter your user name: ").lower()
        if user_name_input in user_name:
            user_password_input = input("Enter your password: ")
            while user_password_input != user_password[user_name.index(user_name_input)]:
                print("Wrong password")
                user_password_input = input("Enter your password: ")
            print("Welcome, " + user_name_input)
        else:
            print("Invalid user name")
            return 0
