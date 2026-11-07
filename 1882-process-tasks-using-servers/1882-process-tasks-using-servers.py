import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)

        ans = []
        t = 0  # ← persistent time, never goes backward

        for j, duration in enumerate(tasks):
            t = max(t, j)  # ← advance to task arrival (or stay if already ahead)

            # If no free servers, jump to next release
            if not free:
                t = max(t, busy[0][0])

            # Release all servers free by time t
            while busy and busy[0][0] <= t:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            # Assign to best free server
            w, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (t + duration, w, idx))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna