class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary(arr,low,high,target):
            if low > high:
                return -1
            
            mid = int((low + high) / 2)

            if arr[mid] == target:
                return mid

            elif target > arr[mid]:
                return binary(arr,mid+1,high,target)

            return binary(arr,low,mid - 1,target)
        low= 0
        high = len(nums) - 1
        return binary(nums,low,high,target)

        

