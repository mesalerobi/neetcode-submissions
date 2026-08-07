class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sort1 = ''.join(sorted(s))
        sort2 = ''.join(sorted(t))

        if sort1 == sort2:
            return True

        return False
        