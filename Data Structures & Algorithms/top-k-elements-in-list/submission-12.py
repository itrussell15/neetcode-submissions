class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        locations = [[] for _ in range(len(nums))]
        for value, count in counts.items():
            locations[count-1].append(value)
        
        result = []
        i = len(locations) - 1
        while len(result) < k:
            result.extend(locations[i])
            i -= 1
        return result
        