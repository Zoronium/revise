# Program: Armstrong Number


# Function to check if a number is an Armstrong number
def is_armstrong(n):
    num_digits = len(str(n))
    sum = 0
    for digit in str(n):
        sum += int(digit) ** num_digits
    return sum == n


# Input a number from the user
number = int(input("Enter a number to check if it's an Armstrong number: "))

# Call the function to check if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
