class Solution:
    def maxDepth(self, s: str) -> int:
        depth = best = 0
        for ch in s:
            if ch == '(':
                depth += 1
                best = max(best, depth)
            elif ch == ')':
                depth -= 1
        return best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna