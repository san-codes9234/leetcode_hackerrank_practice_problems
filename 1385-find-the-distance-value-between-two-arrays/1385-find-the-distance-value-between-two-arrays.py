from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            i = bisect_left(arr2, x)
            # Check nearest neighbours on both sides
            left_ok  = i == 0           or abs(x - arr2[i-1]) > d
            right_ok = i == len(arr2)   or abs(x - arr2[i])   > d
            if left_ok and right_ok:
                count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna