class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(arr, day, m, k):
            count = 0
            bouquets = 0

            for i in range(len(arr)):

                if arr[i] <= day:
                    count += 1

                else:
                    bouquets += count // k
                    count = 0

            bouquets += count // k

            return bouquets >= m

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:

            mid = (low + high) // 2

            if possible(bloomDay, mid, m, k):
                high = mid
            else:
                low = mid + 1

        return low