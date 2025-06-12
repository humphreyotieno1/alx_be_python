def safe_divide(numerator, denominator):
    """
    Performs division, handling division by zero and non-numeric input errors.
    Returns the result or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        # return result
        print(f"The result of the division is {result}")
