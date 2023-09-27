# create sum series like 
# 1 + 1/2 + 1/4 + 1/8 ... + 1/N


n = int(input("Enter a number : "))
x=1
for i in range(n):
   x=x+(1/2**i) 
   print("x",x)

print("Sum of the series:", x)