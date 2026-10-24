class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_s = set(nums)
        longest = 0
        for num in nums_s:
            if (num-1) not in nums_s:
                length = 1
                while (num+length) in nums_s:
                    length += 1

                longest = max(longest, length)
        return longest
