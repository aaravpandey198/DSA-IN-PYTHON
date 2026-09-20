class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generateRow(row):
            ans = 1
            ansRow = [1]

            for col in range(1, row):
                ans = ans * (row - col)
                ans = ans // col
                ansRow.append(ans)

            return ansRow


        def pascalTriangle(N):
            ans = []

            for i in range(1, N + 1):
                ans.append(generateRow(i))

            return ans
        
        return pascalTriangle(numRows)