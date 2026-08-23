class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i, j = 0,0
        n, m = len(nums1), len(nums2)

        while i < n and j < m :
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            
            else:
                result.append(nums2[j])
                j += 1
        if i < n:
            while i < n:
                result.append(nums1[i])
                i += 1

        if j < m:
            while j < m:
                result.append(nums2[j])
                j += 1

        n = len(result)

        if n % 2 != 0:
            median = result[n // 2]
        else:
            median = (result[n // 2 - 1] + result[n // 2]) / 2

        return median