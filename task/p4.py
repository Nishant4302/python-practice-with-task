import random
import clrprint as clr
import time

listcolor = ["red", "green", "blue", "purple", "default", "magenta", "yellow"]
codes = ["\u2764", "\u2703", "\u0407", "\u8304", "\u7779", "\u1603"]
# while True:
#     time.sleep(0.001)
#     clr.clrprint(random.choice(codes),clr=random.choice(listcolor), end=" ")
    

code=[]
for i in range(1):
    a= random.randint(0000,9999)
    a=str(a)
    x= chr(int(92)) +chr(int("117"))+a
    x= str(x)
    code.append(x)
    v= eval(str(code))
    # eval
    print(x, code, v)
# while True:
#     time.sleep(0.001)
#     clr.clrprint(random.choice(code),clr=random.choice(listcolor), end=" ")

