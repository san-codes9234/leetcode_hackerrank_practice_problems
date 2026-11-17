class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):   # length >= 2 required
                l = j - i + 1
                min_cost = float('inf')

                for d in range(1, l):   # d must be < length
                    if l % d != 0:
                        continue

                    changes = 0
                    for g in range(d):  # each group offset g in 0..d-1
                        # collect chars: s[i+g], s[i+g+d], s[i+g+2d], ...
                        group = [s[i + g + step * d]
                                 for step in range(l // d)]

                        # min changes to make group a palindrome
                        m = len(group)
                        for p in range(m // 2):
                            if group[p] != group[m - 1 - p]:
                                changes += 1

                    min_cost = min(min_cost, changes)

                cost[i][j] = min_cost

        # dp[i][j] = min cost to partition s[0..i-1] into j semi-palindromes
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # last part = s[m..i-1], needs length >= 2 → m <= i-2
                for m in range(j - 1, i - 1):
                    if dp[m][j - 1] < INF:
                        dp[i][j] = min(dp[i][j],
                                       dp[m][j - 1] + cost[m][i - 1])

        return dp[n][k]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna