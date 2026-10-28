def factorial(n):
    """Calculates the factorial of a number (e.g., 5! = 5*4*3*2*1)"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
test_num = 5
print(f"The factorial of {test_num} is: {factorial(test_num)}")
