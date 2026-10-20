class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << (seat - 2))
        answer = 2 * (n - len(rows))

        left = 0b00001111   
        middle = 0b00111100  
        right = 0b11110000  

        for mask in rows.values():
            if mask & left == 0 and mask & right == 0:
                # Both sides are available
                answer += 2
            elif mask & left == 0 or mask & middle == 0 or mask & right == 0:
                # At least one arrangement is available
                answer += 1

        return answer
