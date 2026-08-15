class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for n in counts:
            bucket[counts[n]].append(n)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res