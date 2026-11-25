import random
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = (1 << 61) - 1
        BASE = random.randint(10**5 + 1, 10**9)

        def has_unique(length: int) -> bool:
            power = pow(BASE, length, MOD)
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            seen = {h}
            dup = set()

            for i in range(length, n):
                h = (h * BASE - nums[i - length] * power + nums[i]) % MOD
                if h in seen:
                    dup.add(h)
                else:
                    seen.add(h)

            return len(seen) > len(dup)

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna