class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrds = {} # Letter Counts -> [Word, Word, ...]
        for wrd in strs: # Iterate through list of words
            counts = [0] * 26 # Track letter frequency in word
            for ch in wrd: # Iterate through word by character
                counts[ord(ch) - ord('a')] += 1 # Increment frequency of letter
            if tuple(counts) in wrds: # Append word to list if frequency exists
                wrds[tuple(counts)].append(wrd)
            else: # Or add frequency as a new key
                wrds[tuple(counts)] = [wrd]
        return list(wrds.values())