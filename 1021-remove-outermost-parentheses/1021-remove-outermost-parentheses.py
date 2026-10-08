class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:       # not the outermost '('
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:       # not the outermost ')'
                    result.append(ch)

        return "".join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna