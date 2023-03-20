
def replace_word():
    replace_with = ["chief", "thief", "superintendent",
                    "sweeper", "married", "left", "tried", "died"]

    s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

    s.replace("a", "brother")

    words = s.split(" ")
    for i in range(len(words)):
        if words[i] in replace_with:
            words[i] = replace_with[replace_with.index(words[i]) + 1]

    print(" ".join(words))

replace_word()