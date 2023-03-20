def timer(func):
    def inner():
        print('Time start')
        func()
        print('Time end')
    return inner


@timer
def get_factorial():
    print('Factorial')


# timer(get_factorial)()
get_factorial()
