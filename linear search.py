# Program: Linear Search


# Function to perform linear search
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Input a list of numbers and a target number from the user
input_list = list(map(int, input("Enter a list of numbers: ").split()))
target = int(input("Enter a number to search in the list: "))

# Call the function to perform linear search
result = linear_search(input_list, target)

# Print the result
if result == -1:
    print(f"{target} not found in the list.")
else:
    print(f"{target} found at index {result} in the list.")
