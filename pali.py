# Program: Palindrome
# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]


# Input a word from the user
input_word = input("Enter a word to check if it's a palindrome: ")

# Call the function to check if the word is a palindrome
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")
