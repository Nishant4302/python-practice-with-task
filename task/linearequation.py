# Create a program that solves a linear equation of the form ax + b = 0. Prompt the user for the values of coefficients a and b, and then calculate and display the solution for x.

def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions (0 = 0)"
        else:
            return "No solution (0 = {} is not possible)".format(b)
    else:
        x = -b / a
        return "Solution: x = {}".format(x)
   
def main():
    print("Linear Equation Solver: ax + b = 0")
    a = float(input("Enter the coefficient 'a': "))
    b = float(input("Enter the coefficient 'b': "))
    
    solution = solve_linear_equation(a, b)
    print(solution)


main()