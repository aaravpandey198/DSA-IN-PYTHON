class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            row = 0
            for i in range(m):
                if mat[i][mid] > mat[row][mid]:
                    row = i

            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if mid < n - 1 else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < right:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]