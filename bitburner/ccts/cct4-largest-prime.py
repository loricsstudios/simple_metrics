def largest_prime_factor(n):
    largest_factor = 1
    
    # Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    
    # Check for odd factors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n = n // i
    
    # If n is still greater than 2, it's prime
    if n > 2:
        largest_factor = n
    
    return largest_factor

number = 953330869
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")