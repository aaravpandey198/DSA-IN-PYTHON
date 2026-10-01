class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range (len(nums)):
            if nums[i] == target:
                return True
                break
            else:
                continue
        return False
        