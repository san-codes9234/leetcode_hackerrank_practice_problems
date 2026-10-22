class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)

    for i in range(1, n):
      diff = abs(nums[i] - nums[i - 1])
      if diff != 1 and diff != n - 1:
        return -1

    if nums[0] == 0 and nums[-1] == n - 1:
      return 0

    x = nums.index(n - 1)
    return min(x + 1, n - x + 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna