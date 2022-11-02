# Python Exercises for Beginners

# 1. Variables
# Assign values to two variables, then print the sum of the variables.
a = 10
b = 20
sum = a + b
print(sum)

# 2. Data Types
# Store a string, an integer, and a float in three different variables, then print the data type of each variable.
string = "Hello, World!"
integer = 10
floating = 10.5

print(type(string))
print(type(integer))
print(type(floating))

# 3. Basic Operators
# Perform all basic arithmetic operations (addition, subtraction, multiplication, division, modulus, exponentiation, floor division) and print the results.
add = 2 + 3
sub = 5 - 2
mul = 2 * 3
div = 6 / 3
mod = 7 % 3
exp = 2 ** 3
floor_div = 7 // 3

print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(exp)
print(floor_div)

# 4. Conditional Statements
# Write a program that prints "Adult" if the user's age is 18 or above, otherwise it prints "Minor".
age = 25
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 5. Loops
# Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# 6. Functions
# Write a function that greets the user by name.
def greet(name):
    print("Hello, " + name)

greet("John Doe")

# 7. Built-in Functions
# Use built-in functions to get the length, maximum, minimum, and sum of a list of numbers.
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
