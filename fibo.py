# Program: Fibonacci Sequence


# Function to generate the Fibonacci sequence
def fibonacci_sequence(n):
    # Initialize two variables with the first two numbers in the sequence
    a, b = 0, 1
    # Use a for loop to iterate n-1 times
    for i in range(n - 1):
        # Calculate the next number in the sequence and update the variables
        c = a + b
        a = b
        b = c
        print(c, end=", ")
    print()


# Input a number from the user
number = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Call the function to generate the Fibonacci sequence
print("Fibonacci sequence:")
fibonacci_sequence(number)
