class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        index = 0
        max = nums[0]
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                index = i

        return index
        