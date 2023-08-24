temp = int(input("Enter a current temp :"))
c_f= input("enter you are entering temp is C or F :")
c_f=c_f.upper()
if c_f == "C":
    f= (temp*9/5) + 32 
    print(f,"F")
elif c_f == "F":
    c = (temp-32)* 5/9
    print(c,"C")



