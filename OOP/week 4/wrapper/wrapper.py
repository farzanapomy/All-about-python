def do_something(work):
    print("Start the task")
    work()
    print("Finish the task")


def take_parameter():
    print("Hello i am taking parameter successfully")


# do_something(take_parameter)


def first_function():
    print("Hello i am the first function")

    def second_function():
        print("Hello i am the second function")
    return second_function


# call_function = first_function()
# call_function()
first_function()()
