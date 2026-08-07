class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}
        for i, num in enumerate(nums):
            if num not in cache:
                cache[target-num] = i
            else:
                return [cache[num], i]
