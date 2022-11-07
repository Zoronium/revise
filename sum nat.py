def sum_of_naturals(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        return sum


# Input a number from the user
number = int(input("Enter a number to calculate the sum of natural numbers upto it: "))

# Call the function to calculate the sum of natural numbers
print(f"Sum of natural numbers upto {number}:")
print(sum_of_naturals(number))
