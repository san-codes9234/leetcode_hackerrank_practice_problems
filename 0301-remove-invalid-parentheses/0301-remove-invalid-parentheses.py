class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(t: str) -> bool:
            bal = 0
            for ch in t:
                if ch == '(':   bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0: return False
            return bal == 0

        # BFS level by level — first level with valid strings is the answer
        visited = {s}
        queue = [s]

        found = False
        result = []

        while queue:
            next_level = []
            for curr in queue:
                if is_valid(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue  # don't generate children if answer found at this level
                for i in range(len(curr)):
                    if curr[i] not in ('(', ')'):
                        continue
                    candidate = curr[:i] + curr[i+1:]
                    if candidate not in visited:
                        visited.add(candidate)
                        next_level.append(candidate)
            if found:
                return result
            queue = next_level

        return [""]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna