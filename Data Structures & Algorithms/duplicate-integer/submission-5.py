class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = {}
        for n in nums:
            if n in prev:
                return True
            prev[n] = 1
        return False