n= int(input("Enter a number of works : "))

dic={}


for i in range(n):
    work = input('Enter the work: ')
    flag = int(input("when your work is complte press 1 otherwise 0 :"))
    if flag == 1:
        f = True
    else:
        f = False
    d={
        "work title":work,
        "work done":f
    }
    dic[i]=d
      
for i in dic:
    print(dic[i])

