import math
import time


def timer(func):
    def inner(*args, **kwargs):
        print('Time start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time end.total time taken{end-start}')
    return inner


@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'Factorial is {n} of {result}')


# timer(get_factorial)()
get_factorial(n=5)
