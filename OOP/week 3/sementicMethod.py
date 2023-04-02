class Shopping:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    @staticmethod
    def multiply(x, y):
        return x*y

    def add_to_total(self, amount):
        self.total += amount

    def add_to_cart(self, item, quantity, price):
        item_total = price*quantity
        self.add_to_total(item_total)
        self.items.append(item)
        self.customer = "customer"


result = Shopping.multiply(2, 3)
print(result)

result2 = Shopping.add_to_total(2, 3)
print(result2)
