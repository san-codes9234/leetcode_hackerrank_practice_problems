class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1      # last real element in nums1
        p2 = n - 1      # last element in nums2
        p = m + n - 1   # last position in nums1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna