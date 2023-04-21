class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f'{self.buyer} added {item} to cart')


shopper1 = Shop('John')
shopper1.add_to_cart('apple')
print(shopper1.cart)
