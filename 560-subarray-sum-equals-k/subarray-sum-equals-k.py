class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        freq = {0:1}

        prefix_Sum = 0
        count = 0

        for i in range(len(nums)):

            prefix_Sum += nums[i]

            remove = prefix_Sum - k

            if remove in freq:
                count += freq[remove]

            freq[prefix_Sum] = freq.get(prefix_Sum, 0) + 1

        return count