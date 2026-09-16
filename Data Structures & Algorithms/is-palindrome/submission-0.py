class Solution:
    def isPalindrome(self, s: str) -> bool:
        forw = ''.join(filter(str.isalnum, s))
        rev = forw[::-1]
        return forw.lower() == rev.lower()
        