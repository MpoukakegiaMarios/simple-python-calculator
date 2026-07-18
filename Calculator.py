def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y, or None if dividing by zero."""
    if y == 0:
        return None
    return x / y

def calculator():
    # Map choices to a tuple of (function, symbol)
    ops = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }

    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in ops:
            print("Invalid choice. Please select 1-5.")
            continue

        # Keep asking for numbers until input is valid
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break

            except ValueError:
                print("Invalid input! Please enter numeric values only.")

        # Perform the calculation
        func, symbol = ops[choice]
        result = func(num1, num2)

        if result is None:
            print("Error: Cannot divide by zero.")

        else:
            # :g formats the numbers cleanly (removes unnecessary trailing zeros)
            print(f"Result: {num1:g} {symbol} {num2:g} = {result:g}")

if __name__ == "__main__":
    calculator() 

