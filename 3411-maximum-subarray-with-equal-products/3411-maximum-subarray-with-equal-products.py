from math import gcd, lcm
from functools import reduce

class Solution:
    def maxLength(self, nums: int) -> int:
        n = len(nums)
        best = 1
        
        for i in range(n):
            prod = g = l = nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if prod == l * g:
                    best = max(best, j - i + 1)
        
        return best 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna