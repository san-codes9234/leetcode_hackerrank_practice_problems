class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        result = [0] * n
        sorted_pairs = sorted(enumerate(nums), key=lambda x: x[1])

        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][1] - sorted_pairs[j-1][1] <= limit:
                j += 1

            group = sorted_pairs[i:j]
            indices = sorted(p[0] for p in group)
            values  = [p[1] for p in group]
            for idx, val in zip(indices, values):
                result[idx] = val

            i = j

        return result
