class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = [[] for _ in range(len(nums))]

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for value in counts:
            frequencies[counts[value]-1].append(value)
        
        result = []
        idx = len(nums) - 1
        while len(result) < k:
            result.extend(frequencies[idx])
            idx -= 1
        return result
