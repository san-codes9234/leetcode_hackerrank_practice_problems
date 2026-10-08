class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for ch in s:
            if ch=='(':
                if count>0:
                    res.append(ch)
                count+=1
            else:
                count-=1
                if count>0:
                    res.append(ch)
        return "".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna