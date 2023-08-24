user_input = input("Enter a string: ")
if user_input == user_input[::-1]:
    print(f"The word, {user_input}, is a palindrome.")
else:
    print (f"{user_input} is not a palindrome")