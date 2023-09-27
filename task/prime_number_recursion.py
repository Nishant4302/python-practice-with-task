def is_prime(number, divisor=2):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % divisor == 0:
        return False
    if divisor * divisor > number:
        return True
    return is_prime(number, divisor + 1)

# Input the number to check for primality
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
