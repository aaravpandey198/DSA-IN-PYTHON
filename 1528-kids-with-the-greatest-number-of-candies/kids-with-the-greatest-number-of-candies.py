class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_list = []
        highest_candies = candies[0]

        i = 0
        while i < len(candies):
            if candies[i] > highest_candies:
                highest_candies = candies[i]
            i += 1

        for i in range(len(candies)):
            bool_list.append(candies[i] + extraCandies >= highest_candies)

        return bool_list