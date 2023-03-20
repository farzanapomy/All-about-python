# import pyjokes
# def joker_boss():
#     print(pyjokes.get_joke())

# joker_boss()

# exam-3
# def print_hi():
#     return "hi"

# print(print_hi())

# qus-5
# def create_list():
#     x = {'!': 1, '@': 2, '#': 3, '$': 4, '%': 5, '^': 6}
#     output = []
#     for key, value in x.items():
#         output.append(key)
#         output.append(value)
#     print(output)
# create_list()


# qus-6
# def clean_string(s):
#     ans = ""
#     for c in s:
#         if (ord(c) >= 65 and ord(c) <= 90):
#             ans += c
#         elif (ord(c) >= 97 and ord(c) <= 122):
#             ans += c
#     return ans
# s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
# output = clean_string(s)
# print(output)

# qus-7
# Complete the following code (without using the replace function)

# def replace_comma_with_space(text):
#     ans = ""
#     for c in text:
#         if (c == ","):
#             ans += " "
#         else:
#             ans += c
#     return ans
# s = "I,have,been,practising,python,since,the,course,started"

# output = replace_comma_with_space(s)
# print(output)


# qus-8

# def replace_word():
#     replace_with = ["chief", "thief", "superintendent",
#                     "sweeper", "married", "left", "tried", "died"]

#     s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

#     s.replace("a", "brother")

#     words = s.split(" ")
#     for i in range(len(words)):
#         if words[i] in replace_with:
#             words[i] = replace_with[replace_with.index(words[i]) + 1]

#     print(" ".join(words))

# replace_word()


# Qus-10


def create_new_string():
    a = ['oh', 'Emelia', 'to']
    new_a = list(map(str.lower, a))


    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


    words = s.split(" ")


    new_string = ""
    f = open("out.txt", "a")
   
    for i in range(len(words)):
        low = words[i].lower()
        low = (low.replace(",", ""))
        low = (low.replace(".", ""))
        if low in new_a:
            new_string += words[i+1] + " "


    f.write(new_string)
    f.close()




create_new_string()
