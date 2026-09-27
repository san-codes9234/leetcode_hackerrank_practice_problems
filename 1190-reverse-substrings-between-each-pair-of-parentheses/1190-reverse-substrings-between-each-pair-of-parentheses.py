class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                top = stack.pop()[::-1]
                stack[-1].extend(top)
            else:
                stack[-1].append(ch)

        return "".join(stack[0])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna