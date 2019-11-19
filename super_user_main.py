from super_user_class import SuperUser
user_name = ["ahmed", "mohamed"]
user_password = ["000", "111"]

user_1 = SuperUser("Ahmed")
validation = user_1.log_in(user_name, user_password)
while validation == 0:
    validation = user_1.log_in(user_name, user_password)
