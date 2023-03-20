class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_car(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    # def remove_from_cart(self, item):
    #     for i in range(len(self.cart)):
    #         if self.cart[i]['item'] == item:
    #             self.cart.pop(i)
    #             break

    def checkOut(self, amount):
        price = 0
        for item in self.cart:
            print(item)
            price = price+item['price']*item['quantity']

        print(f'Total price : {price} and you pay: {amount}')
        if price > amount:
            return f'Please pay {price-amount} more'
        elif price < amount:
            return f'Please collect your change {amount-price}'
        else:
            return 'Thank you for shopping with us'


shoppingCart = Shopper('John')
shoppingCart.add_to_car('apple', 150, 2)
shoppingCart.add_to_car('HP', 150, 2)
shoppingCart.add_to_car('Lenevo', 150, 2)
shoppingCart.add_to_car('Dell', 150, 2)
shoppingCart.add_to_car('Samsung', 150, 2)
shoppingCart.remove_from_cart('lenovo')
print(shoppingCart.checkOut(900))
