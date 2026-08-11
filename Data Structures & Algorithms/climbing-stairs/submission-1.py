class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 2:
            return n

        one = 1
        two = 1 
        combo = 0

        for i in range(n - 1):
            combo = one + two
            one = two 
            two = combo

        return combo

