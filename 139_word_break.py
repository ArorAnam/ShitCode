# bottom-up approach
# STart from the end of the string and check if the substring from j to i is in the dictionary

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if dp[j + 1] and s[i:j + 1] in wordDict:
                dp[i] = True
                break
    return dp[0]
   
# alternate solution
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[n]