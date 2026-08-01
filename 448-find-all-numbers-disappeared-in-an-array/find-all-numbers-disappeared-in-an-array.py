class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)#code was too slow to run
        missing = []

        for i in range(1, len(nums) + 1):
            if i not in s:
                missing.append(i)

        return missing