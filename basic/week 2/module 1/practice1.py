# 1:
'''
Write a python program that takes a floating number from users using input() and
outputs both Floor and Ceil of that number.
'''
import math;
N=input("Enter a float number: ")
N=float(N)
print("The integer of the input :",math.ceil(N))
print("The integer of the input :",math.floor(N))

# 2:
'''
Write a function that takes inputs from user and
outputs absolute values of these integers without using any
library functions.
'''
N=input("Enter a negative number: ")
N=float(N)
print("The absolute integer of the input :",abs(N))


# 3:
'''
In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
against rock, and scissors wins against paper.
'''
player1=input("Enter player1 name: ")
player2=input("Enter a player2 name: ")

if player1=="Rock" and player2=="scissors":
    print("Player1 wins")
elif player1=="Rock" and player2=="paper":
    print("Player2 wins")
elif player1=="scissors" and player2=="paper":
    print("Player1 wins")


# problem 4
'''Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program.
'''




# practice 5
'''
Write a Python program which iterates the integers from 1 to 50. For multiples of three
print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
which are multiples of both three and five print "FizzBuzz".
'''
for i in range(1,50):
    if i%3==0:
        print("fizz")
        continue
    elif i%5==0:
        print("Buzz")
        continue
    elif i%3==0 and i%5==0:
        print("FizzBuzz")