# fibo
import time
from functools import cache


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# print(fib(10))

start = time.time()

for i in range(10):
    print(i, fib(i))

end_time = time.time()
mil_sec = (end_time-start)*1000
print("Time taken: ", mil_sec, "ms")
