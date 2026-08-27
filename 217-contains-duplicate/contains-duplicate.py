class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for i in freq:
            if freq[i] > 1:
                return True

        return False