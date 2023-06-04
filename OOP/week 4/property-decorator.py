class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f'{self.f_name}.{self.l_name}@user.com'
# to use any method as like attribute we use property decorator

    @property
    def get_fullName(self):
        return f'{self.f_name} {self.l_name}'

    @get_fullName.setter
    def get_fullName(self, value):
        self.f_name = value.split(' ')[0]
        self.l_name = value.split(' ')[1]

    @get_fullName.deleter
    def get_fullName(self):
        self.f_name = None
        self.l_name = None

    def get_email(self):
        return self.email


mark = User('Mark', 'Zuckerberg')
print(mark.email)
print(mark.get_email())
print(mark.get_fullName)
mark.get_fullName = 'Hello boss'
print(mark.get_fullName)
