def minimum_path_sum(triangle):
    # Create a copy of the triangle to store the minimum path sums
    dp = [row[:] for row in triangle]
    
    # Start from the second last row and move upwards
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # The minimum path sum for this position is the value at this position
            # plus the minimum of the two adjacent numbers in the row below
            dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
    
    # The top element now contains the minimum path sum
    return dp[0][0]

# The given triangle
triangle = [
    [4],
    [1,5],
    [7,5,1],
    [6,4,5,9],
    [1,9,2,6,4],
    [8,1,8,5,8,5],
    [6,3,2,3,1,9,8],
    [7,5,6,9,4,8,9,6],
    [5,2,9,4,3,2,3,5,5],
    [4,4,2,6,7,1,1,1,8,6],
    [1,9,4,4,5,3,8,9,2,9,4]
]

result = minimum_path_sum(triangle)
print(f"The minimum path sum is: {result}")