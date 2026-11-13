from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Deque stores [running_max_value, element_count] from left to right (L to R)
        # Values in the deque are strictly increasing from front (left) to back (right)
        q = deque()
        
        r = n - 1
        cost = 0
        ans = 0
        
        for l in range(n - 1, -1, -1):
            x = nums[l]
            count = 1
            
            # Merge blocks from the front whose running max is <= nums[l]
            while q and q[0][0] <= x:
                val, cnt = q.popleft()
                cost += (x - val) * cnt
                count += cnt
            
            q.appendleft([x, count])
            
            # Shrink the right pointer R while total operations exceed k
            while cost > k:
                # The rightmost element nums[r] belongs to the block at the back of the deque
                val, cnt = q[-1]
                cost -= (val - nums[r])
                r -= 1
                if cnt == 1:
                    q.pop()
                else:
                    q[-1][1] -= 1
            
            # All subarrays starting at l and ending anywhere from l to r are valid
            ans += (r - l + 1)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna