s = 'I am feeling very dizzy tonight. But I am sure I did not fire that missile when I was drunk. Being a very professional contract killer I do not fire or plant bombs until particularly needed. Also, I do not have the courage to shoot the President let alone burst a bomb or fire a missle. Stop blaming me or my wrath will burn you into ashes. Ashes is not a brand here, my wrath is like fire, you might die kiddo. So stop pulling my legs and focus on your job. Shoot through the exit now!'

# 1. Write a program to count the number of words in the string.
print((s.split("die")))

# Find the number of dangerous words (die, fire, kill, killer, missile, bomb, burst, shoot, president, burn)  in the string ‘s’ and print them. No words should be printed twice.


for i in s.split():
    if i == 'die' or i == 'fire' or i == 'kill' or i == 'killer' or i == 'missile' or i == 'bomb' or i == 'burst' or i == 'shoot' or i == 'president' or i == 'burn':
        print("Found: ", i)
    # else:
    #     print("Not Found: ", i)


# 4. Write a program to find the number of words that start with a vowel.
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in s.split():
    print(i)
    if i[0] in vowels:
        count += 1
print(count)
