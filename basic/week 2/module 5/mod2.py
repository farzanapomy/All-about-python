numbers=[11,12,13,14,15,16,17]
# numbers={11,12,13,14,15,16,17}

# type 1
def multiply(num):
    total=1
    for num in numbers:
        mul=num*2
        print(mul)
        total+=mul
    # print (total)
# multiply(numbers)

# type 2

def double_it(num):
    return num*num

double_it2=lambda x: x*2

double_it3=map(double_it,numbers)
double_it4=map(lambda x:x*2,numbers)
# print(list(double_it4))

# build=mul()

def filterN(num):
    for num in numbers:
        if num>30:
         print(num)
# filterN(numbers)
filter_number=filter(lambda num: num %2==1,numbers)
# print(list(filter_number))

# dic 
user=[
    {"name":"Farzana","age":30},
    {"name":"manna","age":10},
    {"name":"shabnur","age":15}
    ]
senior_actor = filter(lambda actor: actor["age"]>15,user)
# print(list(senior_actor))

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])
sampleSet = {"Yellow", "Orange", "Black"}
print(list(sampleSet))

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
print((student[1]["age"]))

lamb = lambda x: x ** 3
print(lamb(5))