# create a program that find nearest prime number of given number
x = int(input("enter a number: "))
flag = True
h1 = x
h2 = x

if x > 0:
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            flag = False
            break
    else:
        flag = True
if x ==1:
    print("The prime closest to " + str(x) + " is " + str(x))
if flag:
    print("The prime closest to " + str(x) + " is " + str(x))
elif x>2:
    while not flag:
        h1 -= 1
        for i in range(2, h1):
            if h1 % i == 0:
                flag = False
                break
        else:
            flag = True
            break
    flag=False
    while not flag:
        h2 += 1
        for i in range(2, h2):
            if h2 % i == 0:
                flag = False
                break
        else:
            flag = True
            break
  
    if (x - h1) <= (h2 - x):
        print("The prime closest to", x, "is", h1)
    elif (x - h1) > (h2 - x):
        print("The prime closest to", x, "is", h2)

