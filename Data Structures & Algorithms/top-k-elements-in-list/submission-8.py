class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = [[] for _ in range(len(nums))]

        counts = {}
        for value in nums:
            counts[value] = 1 + counts.get(value, 0)

        for count in counts:
            frequencies[counts[count] - 1].append(count)
        
        result = []
        i = len(frequencies) - 1
        while len(result) < k:
            result.extend(frequencies[i])
            i -= 1
        return result 