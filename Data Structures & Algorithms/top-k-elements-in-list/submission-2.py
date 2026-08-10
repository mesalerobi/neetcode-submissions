class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        bucket = [[] for i in range(len(nums) + 1)] # Frequency -> Number
        for n in nums:
            frq[n] = 1 + frq.get(n, 0)
        for n, f in frq.items():
            bucket[f].append(n)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res