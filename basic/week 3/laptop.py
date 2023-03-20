class Laptop:

    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self, age=1):
        self.age += 1

    def repair(self, life_increase=-5):
        self.increase_age(life_increase)

    def apply_discount(self, num):
        off_price = (self.price * num) / 100
        return self.price - off_price


laptop1 = Laptop("hp", 17)
laptop1.increase_age()
laptop1.increase_age()
laptop1.increase_age()
print(laptop1.age)
laptop1.repair()
print(laptop1.age)
print(laptop1.__dict__)
# laptop1.apply_discount(10)
# print(laptop1.price)
