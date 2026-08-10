class Solution:

    def encode(self, strs: List[str]) -> str:
        wrds = ''
        for w in strs:
            wrds += str(len(w)) + '#' + w
        return wrds

    def decode(self, s: str) -> List[str]:
        wrds = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            wrds.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return wrds
