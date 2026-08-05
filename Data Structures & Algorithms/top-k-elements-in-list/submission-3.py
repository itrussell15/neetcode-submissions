class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Init frequecies counter 
        # [[], [], [], []] - This would initialize for an array of size 4 since we can have a max frequency of 4
        frequencies = [[] for _ in range(len(nums))]

        # Collect the counts of each number
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # Translate counts to frequency counter
        for value in counts:
            frequencies[counts[value]-1].append(value)
        
        # Starting from the highest frequency, go backwards and collect the top k
        result = []
        i = len(frequencies)-1
        while len(result) < k:
            if len(frequencies) > 0:
                [result.append(j) for j in frequencies[i]]
            i -= 1
        return result
