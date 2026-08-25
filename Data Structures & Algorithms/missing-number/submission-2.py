class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        current = set(nums)
        for i in range(len(nums) + 1):
            if i not in current:
                return i
            