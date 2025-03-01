# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result is:", result)
finally:
    print("This block is always executed.")

# Handling multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("The result is:", result)
finally:
    print("This block is always executed.")

# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Age is valid.")

try:
    check_age(-1)
except ValueError as e:
    print("Error:", e)

# Custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("Caught custom exception:", e)