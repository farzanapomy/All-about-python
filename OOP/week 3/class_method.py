class Shopping:
    mall_name = "Jamuna Future Park"
    hours = []

    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def opening_out(cls, day):
        return cls.mall_name + " is open on " + day

    @staticmethod
    def multiply(x, y):
        return x*y

    def add_to_total(self, amount):
        self.total += amount

    def add_to_cart(self, item, price, quantity):
        item_total = price*quantity
        self.add_to_total(item_total)
        # self.prices += item_total
        self.items.append(item)

    def checkOut(self):
        pass


result = Shopping.multiply(2, 3)
print(result)
my_shopping = Shopping("Mark ")
my_shopping.add_to_total(41)
print(my_shopping.total)
