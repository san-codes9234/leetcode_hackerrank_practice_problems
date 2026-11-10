class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # start free

        for j in range(1, n + 1):
            c = costs[j - 1]  # costs is 1-indexed

            # Come from j-1 (penalty = 1² = 1)
            dp[j] = min(dp[j], dp[j-1] + c + 1)

            # Come from j-2 (penalty = 2² = 4)
            if j >= 2:
                dp[j] = min(dp[j], dp[j-2] + c + 4)

            # Come from j-3 (penalty = 3² = 9)
            if j >= 3:
                dp[j] = min(dp[j], dp[j-3] + c + 9)

        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna