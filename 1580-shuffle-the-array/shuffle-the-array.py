class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l3=[]
        l2=[]
        l4=[]
        
        for i in range(int(len(nums)/2)):
            l2.append(nums[i])
            
        for j in range(int(len(nums)/2),len(nums)):
            l3.append(nums[j])
        
        for k in range(int(len(nums)/2)):
            l4.append(l2[k])
            l4.append(l3[k])
        
        return l4