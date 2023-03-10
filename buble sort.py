# Program: Bubble Sort


# Function to sort a list using bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# Input a list of numbers from the user
input_list = list(map(int, input("Enter a list of numbers to sort: ").split()))

# Call the function to sort the list
print(f"Sorted list:")
print(bubble_sort(input_list))
