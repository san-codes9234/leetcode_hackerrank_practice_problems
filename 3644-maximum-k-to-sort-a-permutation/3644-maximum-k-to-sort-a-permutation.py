from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Start with all bits set (-1 in two's complement represents infinite 1s)
        ans = -1
        
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
                
        # If ans is still -1, no elements were misplaced (already sorted)
        return 0 if ans == -1 else ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna