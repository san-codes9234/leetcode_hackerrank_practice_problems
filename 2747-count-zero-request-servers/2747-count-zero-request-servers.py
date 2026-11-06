from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        # Tag queries with original index, sort by value
        sorted_q = sorted(enumerate(queries), key=lambda q: q[1])

        ans = [0] * len(queries)
        freq = defaultdict(int)
        active = 0  # distinct servers in window
        left = right = 0

        for idx, q in sorted_q:
            lo, hi = q - x, q

            # Expand right: add logs with time <= hi
            while right < len(logs) and logs[right][1] <= hi:
                sid = logs[right][0]
                if freq[sid] == 0:
                    active += 1
                freq[sid] += 1
                right += 1

            # Shrink left: remove logs with time < lo
            while left < len(logs) and logs[left][1] < lo:
                sid = logs[left][0]
                freq[sid] -= 1
                if freq[sid] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna