class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        result = []
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if value > len(nums) / 3:
                result.append(key)

        return result