class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #bit wise solution
        #xor operation
        result = 0
        for i in range (len(nums)):
            result = result ^ i ^ nums[i]

        return result ^ len(nums)
