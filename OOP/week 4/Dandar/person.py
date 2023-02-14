# dander , magic method , special method

class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def __add__(self, other):
        return self.money + other.money


person_one = Person("Ellin", 20, 1000)
person_two = Person("Polin", 19, 2000)
person_three = Person("Jolin", 18, 3000)
print(f'{person_one.name} is the friend of {person_two.name}')
print(person_one + person_two)
