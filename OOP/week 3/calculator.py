class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


casio = Calculator()
sum = casio.add(1, 2)
print(sum)

sub = casio.subtract(1, 2)
print(sub)
