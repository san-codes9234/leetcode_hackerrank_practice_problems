import sys
from functools import lru_cache

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        sys.setrecursionlimit(200000)
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dest(i, j, d):  # d=0:right, d=1:down
            if i >= m or j >= n:
                return None
            if grid[i][j] == 0:
                return (i, j)
            return dest(i+1, j, 1) if d == 0 else dest(i, j+1, 0)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue
                for nr, nc, d in ((i, j+1, 0), (i+1, j, 1)):
                    cell = dest(nr, nc, d)
                    if cell:
                        dp[cell[0]][cell[1]] = (dp[cell[0]][cell[1]] + dp[i][j]) % MOD

        return dp[m-1][n-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna