# Write a program that generates the Fibonacci sequence up to a given number 'n'. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. Print the sequence.

n = int( input("Enter a number which you want to print Fibonacci Sequence : "))
n1, n2 =0,1 
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth