class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            current_sum = 0
            subarrays = 1

            for num in nums:

                if current_sum + num <= mid:
                    current_sum += num

                else:
                    current_sum = num
                    subarrays += 1

            if subarrays <= k:
                high = mid
            else:
                low = mid + 1

        return low