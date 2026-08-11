class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones = sorted(stones)
            print(stones)
            stone1 = stones.pop()
            stone2 = stones.pop()
            diff = stone1 - stone2
            if diff > 0:
                stones.append(diff)
        return stones[0] if stones else 0

            

        