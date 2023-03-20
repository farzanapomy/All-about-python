class Cart:

    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, brand):
        self.cart.append(brand)

    def increaseAge(self):
        self.age += 1


shop_1 = Cart('Pom', 1)
shop_1.add_to_cart('Adidas')
shop_1.add_to_cart('Nike')
shop_1.add_to_cart('Puma')

print(shop_1.cart)
