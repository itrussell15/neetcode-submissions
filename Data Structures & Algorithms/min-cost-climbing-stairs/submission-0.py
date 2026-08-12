class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        i = len(cost) - 3
        while i >= 0:
            print(f"{i} - One Step: {cost[i + 1]}, Two Step: {cost[i + 2]}")
            cost[i] = min(cost[i] + cost[i + 1],  cost[i] + cost[i + 2])
            i -= 1
        return min(cost[:2])

