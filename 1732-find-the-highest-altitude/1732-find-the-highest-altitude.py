class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = 0
        maximum = 0
        for g in gain:
            current += g
            maximum = max(maximum, current)
        return maximum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna