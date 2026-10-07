class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        max = nums[0]
        for i in range (len(nums)):
            if nums[i] > max:
                max = nums[i]
        return nums.index(max)
        