# Program: Factorial

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input a number from the user
number = int(input("Enter a number to calculate its factorial: "))

# Call the function to calculate the factorial
print(f"Factorial of {number}:")
print(factorial(number))

