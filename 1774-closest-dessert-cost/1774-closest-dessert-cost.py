class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        self.best = float('inf')

        def dfs(i: int, cost: int):
            if abs(cost - target) < abs(self.best - target) or \
               (abs(cost - target) == abs(self.best - target) and cost < self.best):
                self.best = cost

            if i == len(toppingCosts) or cost >= target:
                return

            for qty in range(3):
                dfs(i + 1, cost + qty * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)

        return self.best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
