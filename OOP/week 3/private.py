# to use hide restricted data from outside of class

class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.phone = phone

    # def get_password(self):
    #     print(self.__password)

    # private method
    def __get_password(self):
        print(self.__password)

    def user_login(self, name, password):
        if name == self.name and password == self.__password:
            print("Login successful")
        else:
            print("Login failed")


dal = User("Dal", "1234", "017000000")
# print(dal.name)
# hack password 
# print(dal._User.__get_password())
# dal.get_password()
result = dal.user_login("Dal", "1234")
