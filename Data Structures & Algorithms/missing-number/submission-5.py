class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for expected, actual in zip(range(len(nums)), nums):
            if actual != expected:
                return expected
            
        return nums[-1] + 1