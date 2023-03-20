myList = ['a', 1, 'b', 2, 'c', 3]

outPut_dict = {}
for index, val in enumerate(myList):
    print(index, val)

    outPut_dict= {val: myList[index+1]} 
    print(outPut_dict)
