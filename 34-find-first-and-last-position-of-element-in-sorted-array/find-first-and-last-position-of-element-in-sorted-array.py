class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def upperbound(arr, x):
            low = 0
            n = len(arr)
            high = n - 1
            ans = n

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] > x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        def lowerbound(arr, x):
            low = 0
            n = len(arr)
            high = n - 1
            ans = n

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] >= x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        lb = lowerbound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        return [lb, upperbound(nums, target) - 1]