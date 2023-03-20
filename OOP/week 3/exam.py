# qus-1
# def exp(a,n):
#     return pow(a,n)

# x, y = input("Enter integers: ").split()
# x = int(x)
# y = int(y)
# print(f"The result is : {exp(x,y)}")


# qus 2. Write a Python program to calculate the sum of a list of numbers.
# def countSum():
#     numbers=input("Enter the numbers: ")
#     numbers=numbers.split("-")

#     sum=0
#     for i in numbers:
#         sum+=float(i)
#     print("The sum is: ",sum)
# countSum()


# qus 3.
# def reverse():
#     s = input("Enter The string: ")
#     s = s.split()

#     for i in s:
#         print(i[::-1], end=" ")
# reverse()


# qus 4.
# def display():
#     s = input("Input String :")
#     list1 = list(s)
#     list2 = []
#     for i in range(0, len(list1), 2):
#         list2.append(list1[i] * int(list1[i+1]))
#     list2.sort(key=str.lower)
#     print("Output :", "".join(list2))
# display()


# qus 5

# import random
# def save_student_data():
#     student_name = input("student name: ")
#     mark = input("mark: ")
#     student_id = random.randint(1000, 9999)
#     with open("student.txt", "a") as f:
#         f.write(
#             f"student Id: {student_id} -> student name ->   {student_name} student mark-> {mark}\n")
# save_student_data()

# def func(arg1, arg2, arg3=4, arg4=5):
#     print(arg1, arg2, arg3, arg4)

# func(3, 4, arg2=1)

# qus 7
# class Subsets:
#     def __init__(self, sub):
#         self.sub = sub

#     def subset(self):
#         return self.subsetsMaker([], sorted(self.sub))

#     def subsetsMaker(self, current, sub):
#         if sub:
#             return self.subsetsMaker(current, sub[1:]) + self.subsetsMaker(current + [sub[0]], sub[1:])
#         return [current]

# print(Subsets([4, 5, 6]).subset())


# qus 8
# class Pairs:
#     def __init__(self, arr, target):
#         self.arr = arr
#         self.target = target
#     def pair(self):
#         for i in range(len(self.arr)):
#             if(self.arr[i] + self.arr[i+1] == self.target):
#                 return i+1, i+2
# pair = Pairs([10, 20, 10, 40, 50, 60, 70], 50).pair()
# print(pair[0], pair[1])


# qus 9

# class SumAndPow:
#     def __init__(self, X, n):
#         self.X = X
#         self.n = n

#     def sum(self):
#         return self.X + self.n

#     def pow(self):
#         return self.X ** self.n


# sum = SumAndPow(3, 4).sum()
# pow = SumAndPow(3, 4).pow()

# print(sum, pow)


# qus 10
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5


print(Distance(2, 3, 4, 5).distance())
