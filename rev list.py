# Program: Reverse a List


# Function to reverse a list
def reverse_list(lst):
    return lst[::-1]


# Input a list from the user
input_list = list(
    map(int, input("Enter a list of numbers separated by space: ").split())
)

# Call the function to reverse the list
print("Reversed list:")
print(reverse_list(input_list))
