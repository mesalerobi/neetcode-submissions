class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrds = defaultdict(list)
        for w in strs:
            counts = [0] * 26
            for l in w:
                counts[ord(l) - ord('a')] += 1
            wrds[tuple(counts)].append(w)
        return list(wrds.values())