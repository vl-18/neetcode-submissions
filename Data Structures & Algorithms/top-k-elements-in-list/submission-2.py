class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]]= seen.get(nums[i],0) + 1

        sorted_seen = sorted(seen, key = lambda n: seen[n], reverse = 'True')
        return sorted_seen[:k]
