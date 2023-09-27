# Create a program that checks if a given string is a palindrome (reads the same forwards and backwards). Prompt the user to enter a string and then determine and display whether the input string is a palindrome or not.

user_input = input("Enter a string: ")
if user_input == user_input[::-1]:
    print(f"The word, {user_input}, is a palindrome.")
else:
    print (f"{user_input} is not a palindrome")