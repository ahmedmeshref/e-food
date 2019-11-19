from user_class import User

class SuperUser(User):
    def log_in(self, user_name, user_password):
        user_name_input = input("Enter your user name: ").lower()
        if user_name_input in user_name:
            user_password_input = input("Enter your password: ")
            if user_password_input == user_password[user_name.index(user_name_input)]:
                print("Welcome, " + user_name_input)
                return 1
            else:
                print("Wrong password")
                return 0
        else:
            print("Invalid user name")
            return 0


