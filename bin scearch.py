# Program: Binary Search


# Function to perform binary search
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Input a sorted list and a target number from the user
input_list = list(
    map(int, input("Enter a sorted list of numbers separated by space: ").split())
)
target = int(input("Enter a number to search in the list: "))

# Call the function to perform binary search
result = binary_search(input_list, target)

# Print the result
if result == -1:
    print(f"{target} not found in the list.")
else:
    print(f"{target} found at index {result} in the list.")
