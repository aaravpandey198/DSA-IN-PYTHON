class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False