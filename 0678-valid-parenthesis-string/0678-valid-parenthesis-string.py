class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0  # range of possible open-paren balances

        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1  # treat as ')'
                hi += 1  # treat as '('

            if hi < 0:
                return False   # even best case has too many ')'
            lo = max(lo, 0)    # balance can't go below 0

        return lo == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna