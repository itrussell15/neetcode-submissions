class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums = sorted(list(set(nums)))
        print(nums)
        
        i = 0 
        count = 0
        max_count = 0
        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i + 1]:
                count +=1 
                max_count = max(count, max_count)
            else:
                count = 0
            i += 1
        return max_count + 1