class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        output = [1, 1]
        for i in range(n - 2):
            new_val = sum(output)
            output.append(new_val)
            output = output[1:]
            # print(output)
        return sum(output)