from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def count(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left  = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            # Choose positions for left among (L+R) slots, recurse on each side
            return comb(len(left) + len(right), len(left)) * count(left) * count(right) % MOD

        return (count(nums) - 1) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna