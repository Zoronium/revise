# Program: Palindrome String

# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Input a string from the user
input_string = input("Enter a string: ")

# Check if the input string is a palindrome and print the result
if is_palindrome(input_string):
    print(input_string + " is a palindrome.")
else:
    print(input_string + " is not a palindrome.")

