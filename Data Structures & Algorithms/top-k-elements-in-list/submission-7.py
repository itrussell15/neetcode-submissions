class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = [[] for _ in range(len(nums))]

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for value in counts:
            frequencies[counts[value]-1].append(value)
        
        final = []
        i = len(frequencies) - 1
        while len(final) < k:
            final.extend(frequencies[i])
            i -= 1
        return final
            