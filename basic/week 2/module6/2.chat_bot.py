
greet_words = ['Hello', 'Hi', 'Hey']
by_words = ['Bye', 'Ta Ta', 'See you']


def listen():
    return input("Say something: ")


def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")

    for word in broken_words:
        # print("He said: ", word)
        if word in "ami dukkhe asi bro":
            talkBack("don't be sad bro")
            return
        elif word in by_words:
            talkBack("He said bye.")
    # print(broken_words)


def talkBack(response):
    print("Bot: ", response)


command = listen()
decide(command)
