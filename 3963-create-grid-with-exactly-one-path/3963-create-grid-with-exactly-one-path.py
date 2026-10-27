class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        r = c = 0
        grid[0][0] = '.'

        # zigzag: right then down, for min(m,n)-1 steps
        for _ in range(min(m, n) - 1):
            c += 1; grid[r][c] = '.'   # go right
            r += 1; grid[r][c] = '.'   # go down

        # go straight to corner
        while c < n - 1:
            c += 1; grid[r][c] = '.'
        while r < m - 1:
            r += 1; grid[r][c] = '.'

        return ["".join(row) for row in grid]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna