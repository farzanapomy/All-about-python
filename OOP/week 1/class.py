class Phone:
    brand = "Walton"
    model = "Primo"
    price = 10000

    def call(self, busy):
        print(busy)

    def wasted_time(self, time):
        print("My total wasted time : ", time*60, "minutes")

    def waste_money(self, money, wasted_time):
        total = (wasted_time*60)*money
        if total > 10000:
            print("You are wasting too much money and time. Shame on you")

        else:
            print("Still You are wasting money and time, but not too much")
        print("See your wasted time", total)


my_phone = Phone()
print(my_phone.brand)

her_phone = Phone()
her_phone.brand = "Samsung"
print(her_phone.brand)
print(my_phone.brand == her_phone.brand)
her_phone.call("Calling...")
my_phone.call("I am busy")
her_phone.call("Okay I will call you later")
her_phone.wasted_time(4)

my_phone.waste_money(4, 10)
