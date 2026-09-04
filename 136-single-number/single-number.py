class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            freq = {}

            for num in nums:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

            for num in freq:
                if freq[num] == 1:
                    return num
