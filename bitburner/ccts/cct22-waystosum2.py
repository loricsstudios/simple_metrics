def count_ways_to_sum(target, nums):
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to create the sum 0: using no elements

    for num in nums:
        for j in range(num, target + 1):
            dp[j] += dp[j - num]

    return dp[target]

# Define the set of integers
nums = [1,3,7,8,9,15,17,19,20,21,22]
# Define the target sum
target_sum = 121

# Calculate the number of distinct ways
number_of_ways = count_ways_to_sum(target_sum, nums)
print(number_of_ways)
