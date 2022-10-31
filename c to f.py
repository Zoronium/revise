# Program: Convert Celsius to Fahrenheit


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Input the temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius to convert it to Fahrenheit: "))

# Call the function to convert Celsius to Fahrenheit
print(f"{celsius}°C in Fahrenheit:")
print(celsius_to_fahrenheit(celsius), "°F")
