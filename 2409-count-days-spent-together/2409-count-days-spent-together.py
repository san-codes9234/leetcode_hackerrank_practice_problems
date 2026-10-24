class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day(date: str) -> int:
            m, d = int(date[:2]), int(date[3:])
            return sum(days[:m-1]) + d
        
        start = max(to_day(arriveAlice), to_day(arriveBob))
        end   = min(to_day(leaveAlice),  to_day(leaveBob))
        
        return max(0, end - start + 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna