
def numDecodings(s):
    if not s:
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if 0 < int(s[0]) <= 9 else 0
    for i in range(2, len(s) + 1):
        if 0 < int(s[i - 1]) <= 9:
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]

# time complexity: O(N), N is the length of the string
# space complexity: O(N), N is the length of the string

# recursive solution:
def numDecodings(s):
    def helper(s, i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        if i == len(s) - 1:
            return 1
        if s[i:i + 2] in {"10", "20"}:
            return helper(s, i + 2)
        if 10 < int(s[i:i + 2]) <= 26:
            return helper(s, i + 1) + helper(s, i + 2)
        return helper(s, i + 1)
    return helper(s, 0)