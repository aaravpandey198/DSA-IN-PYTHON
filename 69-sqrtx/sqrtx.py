class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            for i in range(x):
                if i *i <= x:
                    ans = i
                else:
                    break
        return ans

        
        