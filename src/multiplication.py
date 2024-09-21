# Function to multiply two numbers in python
def multiply(num1, num2):
    return num1 * num2

# Input from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the multiply function
    result = multiply(number1, number2)
    
    # Display the result
    print(f"The result of {number1} * {number2} is: {result}")
except ValueError:
    print("Please enter valid numbers.")
