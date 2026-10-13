class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        counts = Counter(nums)
        
        ladder = [[] for _ in range(len(nums))]
        for count in counts:
            ladder[counts[count]-1].append(count)
        
        output = []
        i = len(ladder) - 1
        while len(output) < k:
            if len(ladder[i]) > 0:
                output.extend(ladder[i])
            i -= 1
        return output