class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones = sorted(stones)
            diff = stones.pop() - stones.pop()
            if diff > 0:
                stones.append(diff)
        return stones[0] if stones else 0

            

        