class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        low = 0
        high = len(height) - 1

        while low < high:
            
            current_height = min(height[low], height[high])
            width = high - low
            area = current_height * width

            max_area = max(max_area, area)

            if height[low] < height[high]:
                low += 1
           
            else:
                high -= 1

        return max_area