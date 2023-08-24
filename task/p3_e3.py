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