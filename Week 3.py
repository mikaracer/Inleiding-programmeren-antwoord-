# Function that takes a string input representing a calculation (e.g., "5+3")
def rekenen(input: str):
    calculation_input = []  # List to store numbers and operator separately
    number = ""  # Temporary string to build numbers from characters

    # Loop through each character in the input string
    for char in input:
        # If the character is a digit or a decimal point, add it to the number
        if char.isdigit() or char == ".":
            number += char
        else:
            # If it's not a digit, we reached an operator (+, -, *, /)
            calculation_input.append(float(number))  # Store the number (as float)
            calculation_input.append(char)  # Store the operator
            number = ""  # Reset number to start reading the next one

    # Append the last number after the loop finishes
    calculation_input.append(float(number))

    # Now calculation_input will look like: [first_number, "operator", second_number]

    # Decide which operation to perform based on the operator
    if calculation_input[1] == "+":
        result = optellen(calculation_input[0], calculation_input[2])  # Addition
    elif calculation_input[1] == "-":
        result = aftrekken(calculation_input[0], calculation_input[2])  # Subtraction
    elif calculation_input[1] == "*":
        result = vermenigvuldigen(calculation_input[0], calculation_input[2])  # Multiplication
    elif calculation_input[1] == "/":
        result = delen(calculation_input[0], calculation_input[2])  # Division

    return result  # Return the calculated result


# Function to add two numbers
def optellen(first_number: float, second_number: float):
    return first_number + second_number


# Function to subtract the second number from the first
def aftrekken(first_number: float, second_number: float):
    return first_number - second_number


# Function to multiply two numbers
def vermenigvuldigen(first_number: float, second_number: float):
    return first_number * second_number


# Function to divide the first number by the second
def delen(first_number: float, second_number: float):
    return first_number / second_number
