# Write a program that takes a number as input and checks if it's a prime number. If the number is prime, print a message stating that; otherwise, print a message stating that the number is not prime.

prime = int(input("Enter a number : "))
flag = 0
if prime>1:
    for i in range (2,int(prime/2)+1):
        if prime%i==0:
            flag=1
            break
        else:
            continue
    if flag == 1:
        print(f'The given number {prime} is not prime')
    else:
        print(f'The given number {prime} is prime')
elif prime == 1:
    print(f'The given number {prime} is not prime')

