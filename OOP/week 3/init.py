class Phone:
    # attributes
    manufactured = 'Nokia'
# method || constructor

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def send_sms(self, number, massage):
        print(f"sending {massage} to {number}...")


# instance

my_phone = Phone("nokia", "1100", 1000)
print(my_phone.manufactured, my_phone.brand)
