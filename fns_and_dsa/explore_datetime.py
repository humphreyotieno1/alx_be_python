from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days):
    """
    Calculate and display a future date by adding the specified number of days to current date.
    
    Args:
        days (int): Number of days to add to the current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()