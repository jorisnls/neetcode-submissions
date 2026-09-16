class Solution:
    def isPalindrome(self, s: str) -> bool:
        forw = ''.join(filter(str.isalnum, s))
        return forw.lower() == forw[::-1].lower()
        