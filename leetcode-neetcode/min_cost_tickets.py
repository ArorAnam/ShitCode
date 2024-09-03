def minCostTickets(days: list[int], costs: list[int]) -> int:
    dp = {}

    def dfs(index):
        if index == len(days): return 0
        if index in dp: return dp[index]

        dp[index] = float("inf")
        for d, c in zip([1,7,30], costs):
            # find index of next day
            next_day = index
            while next_day < len(days) and days[next_day] < days[index] + d: 
                next_day += 1
            dp[index] = min(dp[index], c + dfs(next_day))
        return dp[index]

    return dfs(0) # start at index 0 of days array

days = [1,4,6,7,8,20]
costs = [2,7,15]
res = minCostTickets(days, costs)
print(res)