class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        longest, k = 1, 1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 0:
                continue
            
            elif nums[i+1]-nums[i] == 1:
                k += 1
    
            else:
                k = 1
            
            longest = max(longest, k)
        return longest
