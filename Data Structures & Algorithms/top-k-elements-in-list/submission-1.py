class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for v in nums:
            counts[v] = 1 + counts.get(v, 0)
        for n, c in counts.items():
            buckets[c].append(n)
        ret = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret