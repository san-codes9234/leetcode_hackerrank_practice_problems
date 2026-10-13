class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = 0
        maximum = 0
        for g in gain:
            current += g
            maximum = max(maximum, current)
        return maximum
