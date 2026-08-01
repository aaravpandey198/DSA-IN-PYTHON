class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        l2=[]

        for num in nums:
            
            count=0
            
            for j in range(len(nums)):
               
                if num > nums[j]:
                    count+=1
            
            l2.append(count)    
       
        return l2