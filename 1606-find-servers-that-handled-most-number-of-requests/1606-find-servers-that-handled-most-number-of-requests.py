from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        busy = []  # min-heap: (end_time, server_id)
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            # Release servers that finished by arrival time
            while busy and busy[0][0] <= a:
                end, sid = heapq.heappop(busy)
                free.add(sid)

            if not free:
                continue  # drop request

            # Find next available server >= preferred, wrap if needed
            pref = i % k
            idx = free.bisect_left(pref)
            if idx == len(free):
                idx = 0

            sid = free[idx]
            free.remove(sid)
            count[sid] += 1
            heapq.heappush(busy, (a + l, sid))

        max_req = max(count)
        return [i for i, c in enumerate(count) if c == max_req]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna