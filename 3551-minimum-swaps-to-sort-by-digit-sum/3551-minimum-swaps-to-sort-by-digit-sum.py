class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {v: i for i, v in enumerate(sorted_nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_len += 1
            swaps += cycle_len - 1

        return swaps

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna