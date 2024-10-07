# Get user input for integer and floating-point numbers
a = float(input("Enter a number (a): "))
b = float(input("Enter another number (b): "))
c = int(input("Enter an integer (c): "))


# Import the math module for more advanced math operations
import math

square_root_a = math.sqrt(a)
logarithm_base_10_a = math.log10(a)
factorial_c = math.factorial(abs(c))

print("Square root of a:", square_root_a)
print("Logarithm base 10 of a:", logarithm_base_10_a)
print("Factorial of |c| ({abs(c)}):", factorial_c)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my