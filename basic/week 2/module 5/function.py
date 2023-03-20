def double_it(sum):  
    total=sum+5  
    # print(total)

double_it(5)

def printOutput(sum):
    total=sum*5
    return total

data= printOutput(5)
# print(data)

def mixed(name,*args,**kargs):
    print(name)
    for num in args:
        print(num)
    for key ,value in kargs.items():
        print(kargs)

mixed("farnza","1","2","3","4","5",middle="pomy")
# from function import lab1.py