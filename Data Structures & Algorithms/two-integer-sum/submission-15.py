class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}
        for n, num in enumerate(nums):
            if num in cache:
                return [cache[num], n]
            cache[target-num] = n