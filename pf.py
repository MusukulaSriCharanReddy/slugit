def prime_factors(n):
    """Finds all prime factors of a number"""
    factors = []
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        
    # If n is still greater than 2, then n is prime
    if n > 2:
        factors.append(n)
        
    return factors

# Test the function
test_num = 60
print(f"The prime factors of {test_num} are: {prime_factors(test_num)}")
