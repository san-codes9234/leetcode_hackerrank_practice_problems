class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna