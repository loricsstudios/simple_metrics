def count_partitions(n):
    # dp[i] will be storing the number of partitions of i
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one way to partition 0

    # Loop to calculate the number of partitions for each number from 1 to n
    for i in range(1, n):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    
    # Since we need partitions of at least two integers, subtract 1 for the partition "n" itself
    return dp[n]

# Calculate the number of partitions for 22
result = count_partitions(20)
print(result)
