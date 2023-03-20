# a=input("Enter first number: ")
# b=input("Enter sacend number: ")
# c=input("Enter third number: ")
# quantity = int (a)
# itemno =int(b)
# f =int(c)
# sum=quantity*itemno*price
# celcius = (f-32)*5/9
# print("Total price is: ",celcius)

# live=input("Enter the live: ")
# print(f"He lives in {live}")


# if live=="karachi":
#     print("Hello");


# num=19
# sum=0
# while num<50 :
#     print(num)
#     num+=1
#     sum+=num
    
# print("sum",sum)

# i=1
# while(i<10):
#     print(i,end=" ")
#     i+=1
#     if i==5:
#         break

# name=(6)
for row in range(6):
    for col in range(6):
        if((col==0 or row==0) or (row==3 and col<=5) ):
            print("*",end=" ")
        else:
            print(end="")
    print()

