class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                result.append(depth % 2)  # odd depth → group 0, even → group 1
            else:
                result.append(depth % 2)  # closing bracket matches its opening
                depth -= 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna