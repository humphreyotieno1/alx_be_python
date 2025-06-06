def perform_operation(num1, num2, operation):
    """Function to perform a chosen operation"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 or num2 == 0:
            result = f"Cannot divide by zero"
            return result
        else:
            return num1 / num2
    