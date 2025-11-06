    #TASK 1
num1 = int(input("Enter a number1: "))
if num1 % 2 == 0:
    print(f"{num1} is a Even number")
else:
    print(f"{num1} is a Odd number")

num2 = int(input("Enter a number2: "))
if num2 % 2 == 0:
    print(f"{num2} is a Even number")
else:
    print(f"{num2} is a Odd number")

    # TASK 2
total_sum = 0
for number in range(1,51):
    total_sum += number
    print(f"The sum of number from 1 to 50 is : {total_sum}")
