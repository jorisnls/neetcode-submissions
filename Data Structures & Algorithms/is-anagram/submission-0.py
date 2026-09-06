class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = [0] * 26
        tLetters = [0] * 26
        for c in s:
            sLetters[ord(c)-97] += 1
        for c in t:
            tLetters[ord(c)-97] += 1

        if sLetters == tLetters:
            return True
        return False