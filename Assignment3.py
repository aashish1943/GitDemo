# TASK 1
print("TASK 1")
n = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(f"Factorial of {n} is {factorial(n)}")
print("===================================")

# TASK 2
import math
print("TASK 2")
num = int(input("Enter a number: "))
square_root = math.sqrt(num)
natural_log = math.log(num)
sine = math.sin(num)
print(f"Square root of {num} is {square_root}")
print("--------------------------------------")
print(f"Logarithm of {num} is {natural_log}")
print("--------------------------------------")
print(f"Sine of {num} is {sine}")

