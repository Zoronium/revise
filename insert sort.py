# Program: Insertion Sort


# Function to sort a list using insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# Input a list of numbers from the user
input_list = list(map(int, input("Enter a list of numbers to sort: ").split()))

# Call the function to sort the list
print(f"Sorted list:")
print(insertion_sort(input_list))
