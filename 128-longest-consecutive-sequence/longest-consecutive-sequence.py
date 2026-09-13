class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        count = 0
        last_smaller = float('-inf')

        nums.sort()

        for i in range(len(nums)):
            num = nums[i]

            if num - 1 == last_smaller:
                count += 1
                last_smaller = num

            elif num != last_smaller:
                count = 1
                last_smaller = num

            longest = max(longest, count)

        return longest