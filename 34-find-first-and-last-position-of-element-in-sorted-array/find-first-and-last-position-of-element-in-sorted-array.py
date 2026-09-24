class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left = mid
                l = low
                r = mid - 1

                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        left = m
                        r = m - 1
                    else:
                        l = m + 1

                right = mid
                l = mid + 1
                r = high

                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        right = m
                        l = m + 1
                    else:
                        r = m - 1

                return [left, right]

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return [-1, -1]