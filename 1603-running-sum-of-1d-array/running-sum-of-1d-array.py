class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l2 = []

        for i in range(len(nums)):
            if i == 0:
                l2.append(nums[i])
            else:
                c = nums[i] + l2[i - 1]
                l2.append(c)

        return l2