class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # path length = m+n-1, must be even for valid parentheses
        if (m + n - 1) % 2 == 1:
            return False

        # dp[r][c] = set of possible open-paren balances at (r,c)
        # balance = count of '(' minus count of ')'
        dp = [[set() for _ in range(n)] for _ in range(m)]

        start = 1 if grid[0][0] == '(' else -1
        if start == 1:
            dp[0][0].add(1)
        # if start == -1 (')'), balance is -1 → invalid, skip

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                val = 1 if grid[r][c] == '(' else -1

                # come from top
                if r > 0:
                    for bal in dp[r-1][c]:
                        new = bal + val
                        if new >= 0:
                            dp[r][c].add(new)

                # come from left
                if c > 0:
                    for bal in dp[r][c-1]:
                        new = bal + val
                        if new >= 0:
                            dp[r][c].add(new)

        return 0 in dp[m-1][n-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna