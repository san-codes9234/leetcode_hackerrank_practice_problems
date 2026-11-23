class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [d for d in str(n) if d != '0']
        if not digits:
            return 0
        x = int(''.join(digits))
        return x * sum(int(d) for d in digits)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna