class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for sC in s:
            sMap[sC] = 1 + sMap.get(sC, 0)
        for tC in t:
            tMap[sC] = 1 + tMap.get(tC, 0)
        if sMap.values() != tMap.values():
            return False
        return True