class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in range(len(ransomNote)):
            char = ransomNote[i]

            matchingIndex = magazine.find(char)

            if matchingIndex == -1:
                return False

            magazine = magazine[:matchingIndex] + magazine[matchingIndex + 1:]

        return True
        