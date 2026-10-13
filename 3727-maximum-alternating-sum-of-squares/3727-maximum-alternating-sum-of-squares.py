class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        vals = sorted((abs(x) for x in nums), reverse=True)
        n = len(vals)
        pos_count = (n + 1) // 2   # ceil(n/2)

        result = 0
        for i, v in enumerate(vals):
            if i < pos_count:
                result += v * v   # positive positions
            else:
                result -= v * v   # negative positions
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna