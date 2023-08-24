size = int(input("Enter a size of list : "))
list =[]
# for i in range(size):
#     data = input("Enter a your list element : ")
#     list.append(data)
#     s = set(list)

# print(s)

for i in range(size):
    name = input('Enter a name: ')
    age = input('Enter a age: ')
    phone_number = input('Enter a phone_number: ')
    print(format(name , name))
    print(format(age , age))
    print(format(phone_number, phone_number))
    list.append([name , age, phone_number])
    

        

print(list)



