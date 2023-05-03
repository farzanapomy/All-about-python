class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({"item": item, "price": price, "quantity": quantity})

    def checkOut(self):
        total = 0
        for item in self.cart:
            total = total+item['price']*item['quantity']

        if total > 1000:
            total = total*0.9    
        print(total)

            # total += item["price"] * item["quantity"]
        # print(self.cart)


shopper1 = Shop("John")
shopper1.add_to_cart("apple", 100, 2)
shopper1.add_to_cart("banana", 50, 3)
shopper1.checkOut()
