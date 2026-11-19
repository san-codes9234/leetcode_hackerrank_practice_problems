class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # low score = 0 always achievable (make two elements equal)
        # minimize high score by trimming 2 extremes in 3 ways
        return min(
            nums[n-1] - nums[2],   # cut 2 from left
            nums[n-2] - nums[1],   # cut 1 from each side
            nums[n-3] - nums[0],   # cut 2 from right
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna