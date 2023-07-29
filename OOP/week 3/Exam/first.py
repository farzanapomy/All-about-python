# 1. Create a function exp(a, n) that returns the exponential result ( an ). Read user input a and n in a single line from the keyboard.

def exp(a, n):
    return a**n


print(exp(2, 3))

# 2. Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.


def sum(num):
    sum = 0
    splity = num.split('-')
    print(splity)
    for i in splity:
        sum = sum+float(i)
    print("print", sum)
    return sum


print(sum('2.3-4.5-1.7'), end=' ')
