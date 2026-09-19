class Solution:
    def trap(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while low < high:

            if height[low] <= height[high]:

                if height[low] >= left_max:
                    left_max = height[low]
                else:
                    water += left_max - height[low]

                low += 1

            else:

                if height[high] >= right_max:
                    right_max = height[high]
                else:
                    water += right_max - height[high]

                high -= 1

        return water