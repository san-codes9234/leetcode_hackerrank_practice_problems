class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # Case 1: sorted = rotate_left^k(nums)
        # nums must be a cyclic rotation of [0,1,...,n-1]
        k = (-nums[0]) % n
        if all(nums[j] == (j - k) % n for j in range(n)):
            ans = min(ans, min(k, n - k + 2))

        # Case 2: sorted = rotate_left^k(reverse(nums))
        # nums must be a cyclic rotation of [n-1,...,1,0]
        k = (n - 1 - nums[0]) % n
        if all(nums[m] == (n - 1 - m - k) % n for m in range(n)):
            ans = min(ans, min(k, n - k) + 1)

        return -1 if ans == float('inf') else ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna