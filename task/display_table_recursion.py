def display_table(number, multiplier=1):
    if multiplier <= 10:
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        display_table(number, multiplier + 1)

# Input the number for which you want to display the table
number = int(input("Enter a number: "))

# Call the function to display the table
display_table(number)