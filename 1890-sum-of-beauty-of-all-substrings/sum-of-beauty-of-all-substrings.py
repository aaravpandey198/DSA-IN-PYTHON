
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                maximum = max(freq)
                minimum = float('inf')
                for f in freq:
                    if f > 0:
                        minimum = min(minimum, f)
                ans += maximum - minimum
        return ans
