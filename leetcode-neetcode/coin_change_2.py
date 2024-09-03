from typing import List

class solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]

        # print(dp)    
        return dp[-1]
    

coins = [1,2,5]
amount = 5
res = solution().change(amount, coins)
print(res)