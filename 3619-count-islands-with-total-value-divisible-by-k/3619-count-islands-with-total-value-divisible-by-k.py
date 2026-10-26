class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        def bfs(r, c):
            total = 0
            queue = [(r, c)]
            visited[r][c] = True
            while queue:
                x, y = queue.pop()
                total += grid[x][y]
                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    if bfs(i, j) % k == 0:
                        count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna