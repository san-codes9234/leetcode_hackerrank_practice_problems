class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [sum(grid[i]) for i in range(m)]
        col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        return sum(
            1 for i in range(m) for j in range(n)
            if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1)
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna