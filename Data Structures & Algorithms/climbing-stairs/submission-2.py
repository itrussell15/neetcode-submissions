class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        one = 1
        two = 1
        combo = 0
        for i in range(n - 1):
            tmp = one + two
            one = two
            two = tmp
        return two