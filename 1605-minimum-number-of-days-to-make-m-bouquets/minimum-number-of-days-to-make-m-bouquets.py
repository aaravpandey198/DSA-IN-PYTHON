class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:

            mid = (low + high) // 2

            flowers = 0
            bouquets = 0

            for i in range(len(bloomDay)):

                if bloomDay[i] <= mid:
                    flowers += 1
                else:
                    bouquets += flowers // k
                    flowers = 0

            bouquets += flowers // k

            if bouquets >= m:
                high = mid
            else:
                low = mid + 1

        return low