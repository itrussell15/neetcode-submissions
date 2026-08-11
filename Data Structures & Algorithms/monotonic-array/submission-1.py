class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        increasing = nums[0] < nums[-1]
        for i in range(len(nums)-1):
            val1 = nums[i]
            val2 = nums[i + 1]
            if increasing and val1 > val2:
                return False
            if not increasing and val1 < val2:
                return False
        
        return True


