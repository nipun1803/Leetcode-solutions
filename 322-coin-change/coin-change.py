class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [999999]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] == 999999:
            return -1
        return dp[amount]
