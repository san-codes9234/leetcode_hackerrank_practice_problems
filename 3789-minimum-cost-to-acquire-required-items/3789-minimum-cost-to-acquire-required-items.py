class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(b):
            return (b * costBoth
                    + max(0, need1 - b) * cost1
                    + max(0, need2 - b) * cost2)

        # Check all three breakpoints of the piecewise-linear function
        return min(total(0), total(min(need1, need2)), total(max(need1, need2)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna