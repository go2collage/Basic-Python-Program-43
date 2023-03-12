# Python Function

# Calculate Factorial of a number

def cal_fact(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        return fact


num = int(input("Enter a non-negative Integer number: "))

print("Given number is: ", num)

print(f" {num} Factorial is: ", cal_fact(num))

# thanks for Watching
