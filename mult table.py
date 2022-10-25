# Program: Multiplication Table


# Function to generate the multiplication table for a given number
def generate_multiplication_table(n):
    # Use a for loop to iterate from 1 to 10
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Input a number from the user
number = int(input("Enter a number: "))

# Call the function to generate the multiplication table
print(f"Multiplication table for {number}:")
generate_multiplication_table(number)
