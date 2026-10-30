class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        tmp = [1, 1]
        for i in range(n - 2):
            tmp.append(sum(tmp))
            tmp = tmp[1:]
        return sum(tmp)