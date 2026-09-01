class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        res = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            res[nums[i]] += 1
        for n, c in res.items():
            freq[c].append(n)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans