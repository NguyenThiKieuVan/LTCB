# 1. Handle ZeroDivisionError
def handle_zero_division():
    try:
        num = int(input("Enter a number to divide 10 by: "))
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 2. Raise ValueError if input is not integer
def check_integer_input():
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
    except ValueError:
        print("Error: That is not a valid integer.")

# 3. Raise TypeError if inputs are not numerical
def check_numerical_inputs():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
            raise TypeError("Inputs must be numbers.")
        result = float(a) + float(b)
        print("Sum:", result)
    except TypeError as e:
        print("Error:", e)

# 4. Handle IndexError in list access
def handle_index_error():
    my_list = [10, 20, 30]
    try:
        index = int(input("Enter an index (0-2): "))
        print("Value at index:", my_list[index])
    except IndexError:
        print("Error: Index out of range.")

# 5. Handle KeyboardInterrupt (Ctrl+C)
def handle_keyboard_interrupt():
    try:
        num = input("Enter a number (Ctrl+C to cancel): ")
        print("You entered:", num)
    except KeyboardInterrupt:
        print("\nError: Input cancelled by user.")

# 6. Handle ArithmeticError
def handle_arithmetic_error():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
    except ArithmeticError:
        print("Error: An arithmetic error occurred.")


# Run all functions one by one
if __name__ == "__main__":
    print("\n--- ZeroDivisionError Example ---")
    handle_zero_division()
    
    print("\n--- ValueError Example ---")
    check_integer_input()
    
    print("\n--- TypeError Example ---")
    check_numerical_inputs()
    
    print("\n--- IndexError Example ---")
    handle_index_error()
    
    print("\n--- KeyboardInterrupt Example ---")
    handle_keyboard_interrupt()
    
    print("\n--- ArithmeticError Example ---")
    handle_arithmetic_error()