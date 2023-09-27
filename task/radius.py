# Write a program that prompts the user to input the radius of a circle. Calculate and display both the area (πr^2) and the circumference (2πr) of the circle.
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