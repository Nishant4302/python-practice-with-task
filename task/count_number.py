from array import array

x= array('I', [1,3,1,3,1,1,6,1,5,6,2,4,6,9,6,4,1,6,4,9,6,4,1,9,6,5,4,2,6,4,1,9,6,5,4,9,6,4,1,9,6,4,1,9,6])

countdic={}

def array(x):
    for i  in set(x):   
        countdic[i]=x.count(i)
    k=0
    for i, j in countdic.items():
        if k==0:
            k=j
        elif k <= j :
            k=j
            print(i,"=", j)

array(x)