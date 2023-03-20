# make onelist from two lists
# 2016-03-01    PV

list1 = ['M', 'na', 'i', 'Bo']
list2 = ['y', 'me', 's', 'nd']

list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
 