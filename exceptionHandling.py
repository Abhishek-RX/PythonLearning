num1  = input("Enter a number: ")
num2 = input("Enter second number: ")

try:
    num1= float(num1)
    num2= float(num2)
    result = num1/num2 
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("The result is:", round(result,3))
finally:
    print("This block is always executed.")