from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        return Counter(nums) == Counter(list(range(1, n)) + [n, n])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna