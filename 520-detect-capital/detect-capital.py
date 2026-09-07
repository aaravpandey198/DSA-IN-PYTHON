class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = 0

        for i in range(len(word)):
            if word[i].isupper():
                upper_count += 1

        return (
            upper_count == len(word)
            or upper_count == 0
            or (upper_count == 1 and word[0].isupper())
        )