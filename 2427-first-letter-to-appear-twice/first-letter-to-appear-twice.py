class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hashset = set()

        for i in range(len(s)):
            if s[i] in hashset:
                return s[i]
            else:
                hashset.add(s[i])