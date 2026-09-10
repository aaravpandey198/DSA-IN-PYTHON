class Solution:
    def rearrangeArray(self, nums):
        
        n = len(nums)
        result = [0]*n
        positive_index,negative_index = 0,1
        
        for i in range (0,n):
            if nums[i] >= 0:
                result[positive_index] = nums[i]
                positive_index += 2
            else:
                result[negative_index] = nums[i]
                negative_index += 2
        
        return result
                   