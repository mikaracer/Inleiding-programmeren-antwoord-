# Store an empty list to calculation_history
calculation_history = []

# Start infinite loop
while True:
    # Ask for user input and store as float to n1
    n1 = float(input("Enter the first number (n1): "))
    # Ask for user input and store as float to n2
    n2 = float(input("Enter the second number (n2): "))
    # Ask for user input and store to operation
    operation = input("Enter the operation (add, multiply, divide): ")

    # Check if operation is valid
    if operation in ["add", "multiply", "divide"]:
        # If operation equals "add"
        if operation == "add":
            # Store n1 + n2 to answer
            answer = n1 + n2
            # Print result rounded to 2 decimals
            print(n1, "+", n2, "=", round(answer, 2), "\n")
        # If operation equals "multiply"
        elif operation == "multiply":
            # Store n1 * n2 to answer
            answer = n1 * n2
            # Print result rounded to 2 decimals
            print(n1, "*", n2, "=", round(answer, 2), "\n")
        # Otherwise operation equals "divide"
        else:
            # Check if n2 equals 0
            if n2 == 0:
                # Print error message
                print("You cannot divide by zero!")
                # Continue loop
                continue
            # Store n1 / n2 to answer
            answer = n1 / n2
            # Print result rounded to 2 decimals
            print(n1, "/", n2, "=", round(answer, 2), "\n")
        
        # Append tuple (n1, n2, operation, answer) to calculation_history
        calculation_history.append((n1, n2, operation, round(answer, 2)))
        # Print calculation history
        print("Calculation history:", calculation_history, "\n")
        
        # Ask for user input and store to again
        again = input("Do you want to perform another calculation (yes, no)? ")
        # Check if again is "yes" or "no"
        if again in ["yes", "no"]:
            # If again equals "no"
            if again == "no":
                # Exit program
                exit()
            # Otherwise again equals "yes"
            else:
                # Print separator
                print("---------------------")
        # If again not equal to "yes" or "no"
        else:
            # Print error message
            print("Unexpected answer.")
            # Exit program
            exit()
    # If operation not valid
    else:
        # Print error message
        print("Unexpected operation.")
        # Exit program
        exit()
