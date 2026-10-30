import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][streak] = min cost
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # (cost, node, streak)
        heap = [(0, 0, 1)]   # start at node 0 with streak=1
        dist[0][1] = 0

        while heap:
            cost, u, streak = heapq.heappop(heap)

            if cost > dist[u][streak]:
                continue
            if u == n - 1:
                return cost

            for v, w in graph[u]:
                new_streak = streak + 1 if labels[v] == labels[u] else 1
                if new_streak > k:
                    continue
                new_cost = cost + w
                if new_cost < dist[v][new_streak]:
                    dist[v][new_streak] = new_cost
                    heapq.heappush(heap, (new_cost, v, new_streak))

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna