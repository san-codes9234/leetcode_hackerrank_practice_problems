class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # count how many numbers have each bit set
        bit_count = [0] * 30
        for num in nums:
            for b in range(30):
                if num & (1 << b):
                    bit_count[b] += 1

        # greedily build k numbers: fill from highest bit down
        # for bit b with count c, we can put it in min(c, k) numbers
        result_bits = [0] * k  # result_bits[i] = value of i-th number

        for b in range(29, -1, -1):
            available = min(bit_count[b], k)
            for i in range(available):
                result_bits[i] |= (1 << b)

        return sum(x * x % MOD for x in result_bits) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna