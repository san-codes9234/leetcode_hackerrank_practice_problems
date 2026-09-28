class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # step 1: transpose (swap across main diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # step 2: reverse each row
        for row in matrix:
            row.reverse()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna