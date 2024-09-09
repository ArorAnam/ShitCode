def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]

# Alternate solution
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    first = 1
    second = 2
    for i in range(2, n):
        third = first + second
        first = second
        second = third
    return