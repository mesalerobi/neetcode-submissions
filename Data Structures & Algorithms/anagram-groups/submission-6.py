class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrds = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            wrds[tuple(count)].append(w)
        return list(wrds.values())