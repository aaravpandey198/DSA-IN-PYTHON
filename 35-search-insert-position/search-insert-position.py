class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target in nums:
                return nums.index(target)
            else:
                if target<nums[i]:
                    return i
                elif target not in nums and target>nums[-1]:
                    return len(nums)
        