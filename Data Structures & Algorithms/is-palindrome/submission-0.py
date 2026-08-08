class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointers, one at front and one at back of str
        beg, end = 0, (len(s) - 1)
        # Compare each value (as lowercase)
        while beg < end:
            while beg < end and not self.isAlphaNum(s[beg]):
                beg += 1
            while end > beg and not self.isAlphaNum(s[end]):
                end -= 1
            if s[beg].lower() != s[end].lower():
                return False
            beg, end = beg + 1, end - 1
        return True

    def isAlphaNum(self, ch):
        return (ord('A') <= ord(ch) <= ord('Z') or 
                ord('a') <= ord(ch) <= ord('z') or 
                ord('0') <= ord(ch) <= ord('9'))