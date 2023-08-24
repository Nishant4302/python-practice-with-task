try:
    radius = int(input("Input the radius of a circle : "))

    area  = 3.14*radius*radius
    circumference = 2*3.14*radius
    d={
        "Area" : area,
        "Circumference" : circumference 
    }

    print(d)
except:
    print("Enter a propar data")