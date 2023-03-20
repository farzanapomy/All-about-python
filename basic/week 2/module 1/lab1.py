# # clean code
# data="aHEFK%I$KOSCUP"
# new_date = data.lower()
# length=len(data)
# print(length)

# concat_date=""
# for letter in new_date:
#     if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
#         # print(f"founded {letter}")
#         concat_date+=letter+"_"
#         if (length==0):
#             print("0_")
#         # concat_date=concat_date+" " +letter

# print(concat_date)


# problem 2:
# Encrypt the following code so that no one can get my strategy

# data='az'
# shift=1
# for letter in data:
#     print(ord(letter)+shift-97)
#     print(shift-97)



value=input("Enter the value");
value=int(value)

if value==0:
    print("ZERO")
elif value >=0:
    print(f"{value}positive")
elif value<=0:
    print(f"{value}NEGATIVE")
elif value=='Quit':
     -1
    
