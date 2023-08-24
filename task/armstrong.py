n = int(input("Enter the number to add list : "))
l =[]
for i in range(n):
    y= int(input("Enter a number : "))
    l.append(y)

for x in l:
    print(x, "x")
    orginal_number=x
    count=0 
    while x>0:
        x=x//10
        count+=1
    x=orginal_number
    rev = 0
    while x > 0 :
        digit = x%10
        rev = rev+ pow(digit , count)
        x = x//10
    x=orginal_number    
    if orginal_number==rev:
        print(f"{x} number is armstrong")
    else:
        print(f"{x} number is not armstrong")