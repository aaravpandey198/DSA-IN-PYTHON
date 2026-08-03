class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        duplicate = -1
        missing = -1

        for i in range(1, len(nums)+1):
            if d.get(i,0) == 2:
                duplicate = i
            elif d.get(i,0) == 0:
                missing = i

        return [duplicate, missing]
        #logic bug during testing
    